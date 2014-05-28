def gem_stones(n,strings):
    import _collections
    final_character_count = _collections.defaultdict(int)
    for i in range(n):
        string = strings[i]
        string_character_count = _collections.defaultdict(int)
        for character in string:
            string_character_count[character] += 1
        for character, character_count in string_character_count.iteritems():
            if character_count > 0:
                final_character_count[character] += 1
    gem_stone_count = 0
    for gem,gem_count in final_character_count.iteritems():
        if gem_count == n:
            gem_stone_count += 1

    return gem_stone_count


if __name__ == '__main__':

    strings = []
    n = int(raw_input())
    for i in range(n):
        strings.append(raw_input())

    print gem_stones(n, strings)
