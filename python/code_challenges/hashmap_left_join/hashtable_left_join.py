from python.data_structures.hashtable import Hashtable


def left_join(l_hash, r_hash):
    new_list = []

    hash_left = l_hash.keys()

    for key in hash_left:
        left_key_value = l_hash.get(key)

        right_key_value = "None"

        if r_hash.contains(key):
            right_key_value = r_hash.get(key)
        new_list.append([key, left_key_value, right_key_value])

    return new_list



if __name__ == '__main__':
    l_hash = Hashtable()
    r_hash = Hashtable()
    l_hash.set("diligent", "employed")
    l_hash.set("fond", "enamored")
    l_hash.set("guide", "usher")
    l_hash.set("outfit", "garb")
    l_hash.set("wrath", "anger")
    r_hash.set("diligent", "idle")
    r_hash.set("fond", "averse")
    r_hash.set("guide", "follow")
    r_hash.set("flow", "jam")
    r_hash.set("wrath", "delight")

    print(left_join(l_hash, r_hash))
