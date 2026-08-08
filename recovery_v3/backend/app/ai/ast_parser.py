import tree_sitter_python as tspython
from tree_sitter import Language, Parser

class PythonASTParser:
    def __init__(self):
        self.language = Language(tspython.language())
        self.parser = Parser(self.language)
        
    def chunk_code(self, source_code: bytes, file_path: str) -> list[dict]:
        """
        Parses python code and chunks it into functions and classes.
        """
        tree = self.parser.parse(source_code)
        
        # A simple query to extract functions and classes
        query_string = """
        (function_definition) @function
        (class_definition) @class
        """
        query = self.language.query(query_string)
        
        chunks = []
        matches = query.matches(tree.root_node)
        
        for index, match in enumerate(matches):
            for capture in match[1]:
                node = capture
                chunk_text = source_code[node.start_byte:node.end_byte].decode("utf8")
                
                # A robust chunk should include contextual path info
                header = f"File: {file_path}\nLine: {node.start_point[0]}\n"
                
                chunks.append({
                    "id": f"chunk_{index}",
                    "text": header + chunk_text,
                    "type": node.type,
                    "start_line": node.start_point[0],
                    "end_line": node.end_point[0]
                })
                
        return chunks

ast_parser = PythonASTParser()