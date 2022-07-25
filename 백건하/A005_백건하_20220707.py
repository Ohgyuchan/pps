def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        new = ''
        count = 0
        for one in skill_tree:
            if one in skill:
                new = new + one
                count += 1
        if new == skill[0: count]:
            answer += 1
    return answer