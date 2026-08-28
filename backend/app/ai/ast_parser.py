import importlib
from tree_sitter import Language, Parser, Query, QueryCursor
import logging

logger = logging.getLogger(__name__)

LANGUAGE_QUERIES = {
    "python": """
        (function_definition) @function
        (class_definition) @class
    """,
    "javascript": """
        (function_declaration) @function
        (generator_function_declaration) @function
        (class_declaration) @class
        (lexical_declaration (variable_declarator name: (identifier) value: (arrow_function))) @function
    """,
    "typescript": """
        (function_declaration) @function
        (generator_function_declaration) @function
        (class_declaration) @class
        (interface_declaration) @interface
        (lexical_declaration (variable_declarator name: (identifier) value: (arrow_function))) @function
    """,
    "tsx": """
        (function_declaration) @function
        (class_declaration) @class
        (interface_declaration) @interface
        (lexical_declaration (variable_declarator name: (identifier) value: (arrow_function))) @function
    """,
    "java": """
        (method_declaration) @method
        (class_declaration) @class
        (interface_declaration) @interface
    """,
    "cpp": """
        (function_definition) @function
        (class_specifier) @class
        (struct_specifier) @struct
    """,
    "c": """
        (function_definition) @function
        (struct_specifier) @struct
    """,
    "c-sharp": """
        (method_declaration) @method
        (class_declaration) @class
        (interface_declaration) @interface
    """,
    "go": """
        (function_declaration) @function
        (method_declaration) @method
        (type_declaration) @type
    """,
    "rust": """
        (function_item) @function
        (impl_item) @impl
        (struct_item) @struct
    """,
    "php": """
        (function_definition) @function
        (method_declaration) @method
        (class_declaration) @class
    """,
    "kotlin": """
        (function_declaration) @function
        (class_declaration) @class
    """,
    "swift": """
        (function_declaration) @function
        (class_declaration) @class
        (protocol_declaration) @protocol
    """
}

class ASTParser:
    """
    Tier 1 chunking. Strict AST and symbol extraction using Tree-Sitter.
    Dynamically loads grammar based on language name.
    """
    def __init__(self):
        self.parsers = {}

    def _get_parser(self, lang_name: str) -> Parser:
        if lang_name in self.parsers:
            return self.parsers[lang_name]

        try:
            # Special case for typescript/tsx
            if lang_name in ("typescript", "tsx"):
                ts_module = importlib.import_module("tree_sitter_typescript")
                if lang_name == "typescript":
                    language = Language(ts_module.language_typescript())
                else:
                    language = Language(ts_module.language_tsx())
            else:
                module_name = f"tree_sitter_{lang_name.replace('-', '_')}"
                ts_module = importlib.import_module(module_name)
                language = Language(ts_module.language())
                
            parser = Parser(language)
            self.parsers[lang_name] = (language, parser)
            return language, parser
        except ImportError:
            raise ValueError(f"Tree-sitter grammar for '{lang_name}' not installed.")
        except Exception as e:
            raise ValueError(f"Failed to load grammar for '{lang_name}': {e}")

    def chunk_code(self, source_code: bytes | str, file_path: str, ts_lang_name: str) -> list[dict]:
        """
        Parses code and chunks it into functions, classes, structs, etc.
        """
        if isinstance(source_code, str):
            source_bytes = source_code.encode("utf8", errors="ignore")
        else:
            source_bytes = source_code

        language, parser = self._get_parser(ts_lang_name)
        tree = parser.parse(source_bytes)
        
        query_string = LANGUAGE_QUERIES.get(ts_lang_name)
        if not query_string:
            raise ValueError(f"No semantic query defined for language '{ts_lang_name}'")
            
        try:
            query = Query(language, query_string)
            cursor = QueryCursor(query)
        except Exception as e:
            raise ValueError(f"Query compilation failed for {ts_lang_name}: {e}")

        chunks = []
        matches = cursor.matches(tree.root_node)
        
        for index, match in enumerate(matches):
            captures_dict = match[1]
            for capture_name, nodes in captures_dict.items():
                for node in nodes:
                    chunk_text = source_bytes[node.start_byte:node.end_byte].decode("utf8", errors="ignore")
                    
                    header = f"File: {file_path}\nLine Range: {node.start_point[0] + 1}-{node.end_point[0] + 1}\nLanguage: {ts_lang_name}\n"
                    
                    chunks.append({
                        "id": f"chunk_{index}_{node.start_byte}",
                        "text": header + chunk_text,
                        "type": capture_name,
                        "start_line": node.start_point[0] + 1,
                        "end_line": node.end_point[0] + 1,
                        "processing_tier": 1,
                        "processing_method": "tree_sitter"
                    })
                
        if not chunks:
            raise ValueError(f"No semantic units found in {file_path}")
            
        return chunks

ast_parser = ASTParser()