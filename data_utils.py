"""
데이터 처리를 위한 유틸리티 함수 모음
다양한 데이터 변환 및 검증 기능을 제공합니다.
"""

import json
from typing import List, Dict, Any, Optional
from datetime import datetime


def clean_data(data: List[Dict]) -> List[Dict]:
    """
    데이터 리스트에서 None 값이나 빈 값을 제거합니다.
    
    Args:
        data: 정제할 데이터 리스트
        
    Returns:
        정제된 데이터 리스트
    """
    cleaned = []
    for item in data:
        if item and isinstance(item, dict):
            cleaned_item = {k: v for k, v in item.items() if v is not None and v != ""}
            if cleaned_item:
                cleaned.append(cleaned_item)
    return cleaned


def merge_dictionaries(dict1: Dict, dict2: Dict, overwrite: bool = True) -> Dict:
    """
    두 개의 딕셔너리를 병합합니다.
    
    Args:
        dict1: 첫 번째 딕셔너리
        dict2: 두 번째 딕셔너리
        overwrite: 중복 키 처리 시 덮어쓸지 여부
        
    Returns:
        병합된 딕셔너리
    """
    result = dict1.copy()
    for key, value in dict2.items():
        if key not in result or overwrite:
            result[key] = value
    return result


def validate_email_list(emails: List[str]) -> List[str]:
    """
    이메일 주소 리스트의 유효성을 검증합니다.
    
    Args:
        emails: 검증할 이메일 주소 리스트
        
    Returns:
        유효한 이메일 주소만 포함된 리스트
    """
    valid_emails = []
    for email in emails:
        if "@" in email and "." in email.split("@")[-1]:
            valid_emails.append(email.strip().lower())
    return valid_emails


def calculate_statistics(numbers: List[float]) -> Dict[str, float]:
    """
    숫자 리스트의 통계를 계산합니다.
    
    Args:
        numbers: 통계를 계산할 숫자 리스트
        
    Returns:
        평균, 최소, 최대, 합계를 포함한 딕셔너리
    """
    if not numbers:
        return {"mean": 0, "min": 0, "max": 0, "sum": 0}
    
    return {
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers)
    }


def filter_by_date_range(items: List[Dict], start_date: str, end_date: str, 
                         date_field: str = "date") -> List[Dict]:
    """
    날짜 범위로 아이템을 필터링합니다.
    
    Args:
        items: 필터링할 아이템 리스트
        start_date: 시작 날짜 (YYYY-MM-DD)
        end_date: 종료 날짜 (YYYY-MM-DD)
        date_field: 날짜 필드명
        
    Returns:
        필터링된 아이템 리스트
    """
    filtered = []
    for item in items:
        if date_field in item:
            item_date = item[date_field]
            if start_date <= item_date <= end_date:
                filtered.append(item)
    return filtered


def group_by_key(items: List[Dict], key: str) -> Dict[Any, List[Dict]]:
    """
    특정 키를 기준으로 아이템을 그룹화합니다.
    
    Args:
        items: 그룹화할 아이템 리스트
        key: 그룹화 기준 키
        
    Returns:
        그룹화된 딕셔너리
    """
    groups = {}
    for item in items:
        if key in item:
            group_key = item[key]
            if group_key not in groups:
                groups[group_key] = []
            groups[group_key].append(item)
    return groups


def flatten_nested_dict(nested_dict: Dict, parent_key: str = '', 
                        separator: str = '.') -> Dict:
    """
    중첩된 딕셔너리를 평탄화합니다.
    
    Args:
        nested_dict: 중첩된 딕셔너리
        parent_key: 부모 키
        separator: 키 구분자
        
    Returns:
        평탄화된 딕셔너리
    """
    items = []
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_nested_dict(value, new_key, separator).items())
        else:
            items.append((new_key, value))
    return dict(items)

