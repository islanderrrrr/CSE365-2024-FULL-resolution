# 挑战简介
无需解析的冒泡排序

# 思路
冒泡如下  
```
for ( i = 0; i <= 3; ++i )
  {
    for ( j = 0; j < 4 - i; ++j )
    {
      if ( *((_BYTE *)&buf + j) > *((_BYTE *)&buf + j + 1) )
      {
        v3 = *((_BYTE *)&buf + j);
        *((_BYTE *)&buf + j) = *((_BYTE *)&buf + j + 1);
        *((_BYTE *)&buf + j + 1) = v3;
      }
    }
  }
```

源字符串：jlmny  
输入： 同上  
