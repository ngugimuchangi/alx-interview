#!/usr/bin/python3
"""
Lockboxes 🥡🔒🔑
"""


def canUnlockAll(boxes):
    """ Lockboxes function
        Args:
            - boxes: list of boxes either empty
                     or with one or more keys.
        Return:
            - True or False depending on whether
              all the boxes can be unlocked based
              keys found and where found
    """
    if not boxes:
        return False
    if len(boxes) == 1:
        return True
    unlock_status = {x: True if not x else False for x in range(len(boxes))}
    for box in boxes:
        viable_keys = list(filter(lambda x: all([x > 0, x < len(boxes),
                                                 x != boxes.index(box)]), box))
        unlock_status.update({x: True for x in viable_keys})
    return all(unlock_status.values())
