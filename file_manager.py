"""
파일 관리 헬퍼 모듈
파일 및 디렉토리 작업을 위한 유틸리티 함수들을 제공합니다.
"""

import os
import json
import shutil
from pathlib import Path
from typing import List, Dict, Optional
import hashlib


def get_file_size(filepath: str, unit: str = 'MB') -> float:
    """
    파일의 크기를 지정된 단위로 반환합니다.
    
    Args:
        filepath: 파일 경로
        unit: 크기 단위 (B, KB, MB, GB)
        
    Returns:
        파일 크기
    """
    if not os.path.exists(filepath):
        return 0.0
    
    size_bytes = os.path.getsize(filepath)
    units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3}
    return size_bytes / units.get(unit.upper(), 1024**2)


def list_files_by_extension(directory: str, extension: str) -> List[str]:
    """
    특정 확장자를 가진 모든 파일을 찾습니다.
    
    Args:
        directory: 검색할 디렉토리
        extension: 파일 확장자 (예: '.txt')
        
    Returns:
        파일 경로 리스트
    """
    if not os.path.exists(directory):
        return []
    
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(extension):
                files.append(os.path.join(root, filename))
    return files


def create_directory_tree(base_path: str, structure: Dict) -> None:
    """
    딕셔너리 구조를 기반으로 디렉토리 트리를 생성합니다.
    
    Args:
        base_path: 기본 경로
        structure: 디렉토리 구조 딕셔너리
    """
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_directory_tree(path, content)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(str(content))


def calculate_file_hash(filepath: str, algorithm: str = 'sha256') -> Optional[str]:
    """
    파일의 해시값을 계산합니다.
    
    Args:
        filepath: 파일 경로
        algorithm: 해시 알고리즘 (md5, sha1, sha256)
        
    Returns:
        해시값 문자열
    """
    if not os.path.exists(filepath):
        return None
    
    hash_func = getattr(hashlib, algorithm)()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def backup_file(filepath: str, backup_dir: str = 'backups') -> Optional[str]:
    """
    파일을 백업 디렉토리에 복사합니다.
    
    Args:
        filepath: 백업할 파일 경로
        backup_dir: 백업 디렉토리
        
    Returns:
        백업된 파일의 경로
    """
    if not os.path.exists(filepath):
        return None
    
    os.makedirs(backup_dir, exist_ok=True)
    filename = os.path.basename(filepath)
    backup_path = os.path.join(backup_dir, f"{filename}.bak")
    shutil.copy2(filepath, backup_path)
    return backup_path


def find_duplicate_files(directory: str) -> Dict[str, List[str]]:
    """
    디렉토리 내의 중복 파일을 찾습니다.
    
    Args:
        directory: 검색할 디렉토리
        
    Returns:
        해시값을 키로, 파일 경로 리스트를 값으로 하는 딕셔너리
    """
    hash_dict = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hash = calculate_file_hash(filepath)
            if file_hash:
                if file_hash not in hash_dict:
                    hash_dict[file_hash] = []
                hash_dict[file_hash].append(filepath)
    
    return {k: v for k, v in hash_dict.items() if len(v) > 1}


def get_directory_size(directory: str) -> float:
    """
    디렉토리의 총 크기를 MB 단위로 계산합니다.
    
    Args:
        directory: 디렉토리 경로
        
    Returns:
        디렉토리 크기 (MB)
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.exists(filepath):
                total_size += os.path.getsize(filepath)
    return total_size / (1024 ** 2)


def clean_empty_directories(directory: str) -> int:
    """
    빈 디렉토리를 재귀적으로 삭제합니다.
    
    Args:
        directory: 정리할 디렉토리
        
    Returns:
        삭제된 디렉토리 수
    """
    deleted_count = 0
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                deleted_count += 1
    return deleted_count

