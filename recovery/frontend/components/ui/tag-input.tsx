import React, { useState, KeyboardEvent, useRef, useEffect } from 'react';
import { X, Command } from 'lucide-react';

interface TagInputProps {
  placeholder?: string;
  tags: string[];
  setTags: (tags: string[]) => void;
  disabled?: boolean;
  suggestions?: string[];
}

export function TagInput({ placeholder, tags, setTags, disabled, suggestions = [] }: TagInputProps) {
  const [inputValue, setInputValue] = useState('');
  const [isOpen, setIsOpen] = useState(false);
  const wrapperRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (wrapperRef.current && !wrapperRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [wrapperRef]);

  const filteredSuggestions = suggestions.filter(
    (suggestion) => 
      suggestion.toLowerCase().includes(inputValue.toLowerCase()) && 
      !tags.includes(suggestion)
  );

  const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' || e.key === ',') {
      e.preventDefault();
      const newTag = inputValue.trim();
      if (newTag && !tags.includes(newTag)) {
        setTags([...tags, newTag]);
        setInputValue('');
        setIsOpen(false);
      }
    } else if (e.key === 'Backspace' && !inputValue && tags.length > 0) {
      const newTags = [...tags];
      newTags.pop();
      setTags(newTags);
    }
  };

  const addTag = (tag: string) => {
    if (!tags.includes(tag)) {
      setTags([...tags, tag]);
      setInputValue('');
      setIsOpen(false);
    }
  };

  const removeTag = (indexToRemove: number) => {
    setTags(tags.filter((_, index) => index !== indexToRemove));
  };

  return (
    <div className="relative" ref={wrapperRef}>
      <div className={`flex flex-wrap gap-2 p-2 rounded-md border border-white/10 bg-black/50 ${disabled ? 'opacity-50 cursor-not-allowed' : 'focus-within:ring-1 focus-within:ring-primary focus-within:border-primary'}`}>
        {tags.map((tag, index) => (
          <span key={index} className="flex items-center gap-1 px-2 py-1 text-xs font-medium rounded-md bg-white/5 border border-white/10 text-white">
            {tag}
            {!disabled && (
              <button
                type="button"
                onClick={() => removeTag(index)}
                className="text-muted-foreground hover:text-white transition-colors"
              >
                <X className="w-3 h-3" />
              </button>
            )}
          </span>
        ))}
        <input
          type="text"
          className="flex-1 min-w-[120px] bg-transparent outline-none text-sm placeholder:text-muted-foreground"
          placeholder={tags.length === 0 ? placeholder : ''}
          value={inputValue}
          onChange={(e) => {
            setInputValue(e.target.value);
            setIsOpen(true);
          }}
          onFocus={() => setIsOpen(true)}
          onKeyDown={handleKeyDown}
          disabled={disabled}
        />
      </div>

      {isOpen && filteredSuggestions.length > 0 && !disabled && (
        <div className="absolute z-50 w-full mt-1 bg-[#1a1a1a] border border-white/10 rounded-md shadow-xl overflow-hidden max-h-60 overflow-y-auto">
          {filteredSuggestions.map((suggestion, index) => (
            <div
              key={index}
              className="px-3 py-2 text-sm text-muted-foreground hover:text-white hover:bg-white/5 cursor-pointer flex items-center gap-2"
              onClick={() => addTag(suggestion)}
            >
              <Command className="w-3 h-3 opacity-50" /> {suggestion}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}