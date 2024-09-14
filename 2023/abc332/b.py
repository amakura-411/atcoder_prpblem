K, G, M = map(int, input().split())

g_limit = 0
m_limit = 0

for i in range(K):
    if g_limit == G:  # グラスが満たされている場合
        g_limit = 0
    elif m_limit == 0:  # マグカップが空の場合
        m_limit = M
    else:
        # マグカップからグラスへの水の移し方を修正
        if G - g_limit < m_limit:
            m_limit -= G - g_limit
            g_limit = G
        else:
            g_limit += m_limit
            m_limit = 0
    print(g_limit, m_limit)

print(g_limit, m_limit)
