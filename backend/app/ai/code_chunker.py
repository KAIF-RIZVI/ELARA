import re

class CodeChunker:
    """
    Handles Tier 2 (Structure-aware) and Tier 3 (Generic Fallback) chunking.
    """
    
    @staticmethod
    def structure_aware_chunk(source_code: bytes | str, file_path: str, language: str) -> list[dict]:
        """
        Tier 2 chunking. Uses basic heuristics to find structural boundaries for web/config languages.
        """
        if isinstance(source_code, bytes):
            text = source_code.decode("utf8", errors="ignore")
        else:
            text = source_code

        # Determine split pattern based on language
        language = language.lower()
        if language in ("html", "htm", "xml"):
            pattern = r'(?=<[a-zA-Z0-9_-]+)'
        elif language == "json":
            pattern = r'(?=^\s*[{["]\s*)' 
        elif language in ("yaml", "yml"):
            pattern = r'(?=^[a-zA-Z0-9_-]+:)'
        elif language in ("css", "scss"):
            pattern = r'(?=^[.#a-zA-Z0-9_-]+\s*\{)'
        elif language == "markdown" or language == "md":
            pattern = r'(?=^#+\s)'
        else:
            pattern = r'\n\s*\n'

        # Split on common structural boundaries (double newlines, blocks) to preserve logical blocks
        blocks = re.split(pattern, text, flags=re.MULTILINE) if pattern != r'\n\s*\n' else re.split(pattern, text)
        chunks = []
        current_chunk_lines = []
        current_line_count = 1 # 1-indexed
        
        chunk_idx = 0
        
        for block in blocks:
            if not block.strip():
                continue
            lines_in_block = block.split('\n')
            block_line_count = len(lines_in_block)
            
            # If a single block is huge, we preserve boundaries up to ~60 lines
            if len(current_chunk_lines) + block_line_count > 60 and current_chunk_lines:
                header = f"File: {file_path}\nLine Range: {current_line_count}-{current_line_count + len(current_chunk_lines) - 1}\nLanguage: {language}\n"
                chunks.append({
                    "id": f"chunk_{chunk_idx}",
                    "text": header + "\n".join(current_chunk_lines),
                    "type": "structural_block",
                    "start_line": current_line_count,
                    "end_line": current_line_count + len(current_chunk_lines) - 1,
                    "processing_tier": 2,
                    "processing_method": f"{language}_structure_chunker"
                })
                chunk_idx += 1
                current_line_count += len(current_chunk_lines)
                current_chunk_lines = lines_in_block
            else:
                current_chunk_lines.extend(lines_in_block)
                
        if current_chunk_lines:
            header = f"File: {file_path}\nLine Range: {current_line_count}-{current_line_count + len(current_chunk_lines) - 1}\nLanguage: {language}\n"
            chunks.append({
                "id": f"chunk_{chunk_idx}",
                "text": header + "\n".join(current_chunk_lines).strip(),
                "type": "structural_block",
                "start_line": current_line_count,
                "end_line": current_line_count + len(current_chunk_lines) - 1,
                "processing_tier": 2,
                "processing_method": f"{language}_structure_chunker"
            })

        return chunks

    @staticmethod
    def generic_chunk(source_code: bytes | str, file_path: str, chunk_size_lines: int = 50, overlap_lines: int = 10, language: str = "unknown") -> list[dict]:
        """
        Tier 3 chunking. Generic overlapping line chunker.
        """
        if isinstance(source_code, bytes):
            text = source_code.decode("utf8", errors="ignore")
        else:
            text = source_code
            
        lines = text.split("\n")
        chunks = []
        
        i = 0
        chunk_idx = 0
        while i < len(lines):
            end = min(i + chunk_size_lines, len(lines))
            chunk_lines = lines[i:end]
            if not any(l.strip() for l in chunk_lines):
                i += (chunk_size_lines - overlap_lines)
                continue
                
            header = f"File: {file_path}\nLine Range: {i+1}-{end}\nLanguage: {language}\n"
            chunk_text = header + "\n".join(chunk_lines)
            
            chunks.append({
                "id": f"chunk_{chunk_idx}",
                "text": chunk_text,
                "type": "fallback_block",
                "start_line": i + 1,
                "end_line": end,
                "processing_tier": 3,
                "processing_method": "generic_line_chunker"
            })
            
            chunk_idx += 1
            i += (chunk_size_lines - overlap_lines)
            if i >= len(lines) - overlap_lines:
                break
                
        return chunks

code_chunker = CodeChunker()
