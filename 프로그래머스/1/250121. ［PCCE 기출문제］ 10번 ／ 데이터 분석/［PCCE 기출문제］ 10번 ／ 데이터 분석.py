def solution(data, ext, val_ext, sort_by):
    col_idx = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    filtered_data = [row for row in data if row[col_idx[ext]] < val_ext]
    
    filtered_data.sort(key=lambda x: x[col_idx[sort_by]])
    
    return filtered_data