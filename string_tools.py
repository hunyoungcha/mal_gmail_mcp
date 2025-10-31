"""
문자열 처리 도구 모음
다양한 문자열 변환 및 분석 기능을 제공합니다.
"""

import re
from typing import List, Optional


def sanitize_filename(filename: str) -> str:
    """
    파일명에서 사용할 수 없는 문자를 제거합니다.
    
    Args:
        filename: 원본 파일명
        
    Returns:
        정제된 파일명
    """
    invalid_chars = r'[<>:"/\\|?*]'
    sanitized = re.sub(invalid_chars, '_', filename)
    sanitized = sanitized.strip('. ')
    return sanitized if sanitized else 'unnamed'


def extract_urls(text: str) -> List[str]:
    """
    텍스트에서 모든 URL을 추출합니다.
    
    Args:
        text: URL을 추출할 텍스트
        
    Returns:
        URL 리스트
    """
    url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    urls = re.findall(url_pattern, text)
    return urls


def camel_to_snake(text: str) -> str:
    """
    camelCase를 snake_case로 변환합니다.
    
    Args:
        text: 변환할 문자열
        
    Returns:
        snake_case 문자열
    """
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    snake_case = pattern.sub('_', text).lower()
    return snake_case


def snake_to_camel(text: str) -> str:
    """
    snake_case를 camelCase로 변환합니다.
    
    Args:
        text: 변환할 문자열
        
    Returns:
        camelCase 문자열
    """
    components = text.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def truncate_text(text: str, max_length: int, suffix: str = '...') -> str:
    """
    텍스트를 지정된 길이로 자르고 접미사를 추가합니다.
    
    Args:
        text: 자를 텍스트
        max_length: 최대 길이
        suffix: 접미사
        
    Returns:
        잘린 텍스트
    """
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix


def count_words(text: str) -> int:
    """
    텍스트의 단어 수를 계산합니다.
    
    Args:
        text: 단어를 셀 텍스트
        
    Returns:
        단어 수
    """
    words = re.findall(r'\b\w+\b', text)
    return len(words)


def extract_hashtags(text: str) -> List[str]:
    """
    텍스트에서 해시태그를 추출합니다.
    
    Args:
        text: 해시태그를 추출할 텍스트
        
    Returns:
        해시태그 리스트
    """
    hashtags = re.findall(r'#\w+', text)
    return [tag.lower() for tag in hashtags]


def remove_html_tags(html: str) -> str:
    """
    HTML 태그를 제거하고 순수 텍스트만 반환합니다.
    
    Args:
        html: HTML 문자열
        
    Returns:
        태그가 제거된 텍스트
    """
    clean = re.compile('<.*?>')
    return re.sub(clean, '', html)


def is_palindrome(text: str) -> bool:
    """
    문자열이 회문인지 확인합니다.
    
    Args:
        text: 확인할 문자열
        
    Returns:
        회문 여부
    """
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]


def mask_sensitive_data(text: str, mask_char: str = '*') -> str:
    """
    이메일과 전화번호 같은 민감한 데이터를 마스킹합니다.
    
    Args:
        text: 원본 텍스트
        mask_char: 마스킹 문자
        
    Returns:
        마스킹된 텍스트
    """
    # 이메일 마스킹
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    text = re.sub(email_pattern, f'{mask_char * 5}@{mask_char * 5}.com', text)
    
    # 전화번호 마스킹
    phone_pattern = r'\b\d{3}[-.]?\d{3,4}[-.]?\d{4}\b'
    text = re.sub(phone_pattern, f'{mask_char * 3}-{mask_char * 4}-{mask_char * 4}', text)
    
    return text

