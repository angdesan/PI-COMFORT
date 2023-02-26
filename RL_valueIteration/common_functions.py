import datetime

MORNING_HOURS_START = 7
MORNING_HOURS_END = 12
AFTERNOON_HOUR_START = 17
NIGHT_HOUR_END = 24


def get_state(ac_status: int, comfort: int, time: int, tempExt: float) -> int:
    """
    Returns: 
    int: state index [0,108]

    """
    # P1 : 7H00 a 12H00
    if MORNING_HOURS_START <= time < MORNING_HOURS_END:
        if ac_status == 2:  # OFF
            if 18 <= tempExt <= 24:
                if comfort == 0:
                    return 0
                if comfort == 1:
                    return 1
                if comfort == 2:
                    return 2
            if 24 < tempExt <= 29:
                if comfort == 0:
                    return 3
                if comfort == 1:
                    return 4
                if comfort == 2:
                    return 5
            if 29 < tempExt <= 35:
                if comfort == 0:
                    return 6
                if comfort == 1:
                    return 7
                if comfort == 2:
                    return 8
        if 3 <= ac_status <= 5:  # [16,18]
            if 18 <= tempExt <= 24:
                if comfort == 0:
                    return 9
                if comfort == 1:
                    return 10
                if comfort == 2:
                    return 11
            if 24 < tempExt <= 29:
                if comfort == 0:
                    return 12
                if comfort == 1:
                    return 13
                if comfort == 2:
                    return 14
            if 29 < tempExt <= 35:
                if comfort == 0:
                    return 15
                if comfort == 1:
                    return 16
                if comfort == 2:
                    return 17
        if 6 <= ac_status <= 8:  # [19,21]
            if 18 <= tempExt <= 24:
                if comfort == 0:
                    return 18
                if comfort == 1:
                    return 19
                if comfort == 2:
                    return 20
            if 24 < tempExt <= 29:
                if comfort == 0:
                    return 21
                if comfort == 1:
                    return 22
                if comfort == 2:
                    return 23
            if 29 < tempExt <= 35:
                if comfort == 0:
                    return 24
                if comfort == 1:
                    return 25
                if comfort == 2:
                    return 26
        if 9 <= ac_status <= 11:  # [22,24]
            if 18 <= tempExt <= 24:
                if comfort == 0:
                    return 27
                if comfort == 1:
                    return 28
                if comfort == 2:
                    return 29
            if 24 < tempExt <= 29:
                if comfort == 0:
                    return 30
                if comfort == 1:
                    return 31
                if comfort == 2:
                    return 32
            if 29 < tempExt <= 35:
                if comfort == 0:
                    return 33
                if comfort == 1:
                    return 34
                if comfort == 2:
                    return 35
    # P2: 12H00 a 17h00
    if MORNING_HOURS_END <= time < AFTERNOON_HOUR_START:
        if ac_status == 2:  # OFF
            if 18 <= tempExt <= 24:
                if comfort == 0:
                    return 36
                if comfort == 1:
                    return 37
                if comfort == 2:
                    return 38
            if 24 < tempExt <= 29:
                if comfort == 0:
                    return 39
                if comfort == 1:
                    return 40
                if comfort == 2:
                    return 41
            if 29 < tempExt <= 35:
                if comfort == 0:
                    return 42
                if comfort == 1:
                    return 43
                if comfort == 2:
                    return 44
        if 3 <= ac_status <= 5:  # [16,18]
            if 18 <= tempExt <= 24:
                if comfort == 0:
                    return 45
                if comfort == 1:
                    return 46
                if comfort == 2:
                    return 47
            if 24 < tempExt <= 29:
                if comfort == 0:
                    return 48
                if comfort == 1:
                    return 49
                if comfort == 2:
                    return 50
            if 29 < tempExt <= 35:
                if comfort == 0:
                    return 51
                if comfort == 1:
                    return 52
                if comfort == 2:
                    return 53
        if 6 <= ac_status <= 8:  # [19,21]
            if 18 <= tempExt <= 24:
                if comfort == 0:
                    return 54
                if comfort == 1:
                    return 55
                if comfort == 2:
                    return 56
            if 24 < tempExt <= 29:
                if comfort == 0:
                    return 57
                if comfort == 1:
                    return 58
                if comfort == 2:
                    return 59
            if 29 < tempExt <= 35:
                if comfort == 0:
                    return 60
                if comfort == 1:
                    return 61
                if comfort == 2:
                    return 62
        if 9 <= ac_status <= 11:  # [22,24]
            if 18 <= tempExt <= 24:
                if comfort == 0:
                    return 63
                if comfort == 1:
                    return 64
                if comfort == 2:
                    return 65
            if 24 < tempExt <= 29:
                if comfort == 0:
                    return 66
                if comfort == 1:
                    return 67
                if comfort == 2:
                    return 68
            if 29 < tempExt <= 35:
                if comfort == 0:
                    return 69
                if comfort == 1:
                    return 70
                if comfort == 2:
                    return 71

    # P3: 17H00 a 23h59
    if AFTERNOON_HOUR_START <= time < NIGHT_HOUR_END:
        if ac_status == 2:  # OFF
            if 18 <= tempExt <= 24:
                if comfort == 0:
                    return 72
                if comfort == 1:
                    return 73
                if comfort == 2:
                    return 74
            if 24 < tempExt <= 29:
                if comfort == 0:
                    return 75
                if comfort == 1:
                    return 76
                if comfort == 2:
                    return 77
            if 29 < tempExt <= 35:
                if comfort == 0:
                    return 78
                if comfort == 1:
                    return 79
                if comfort == 2:
                    return 80
        if 3 <= ac_status <= 5:  # [16,18]
            if 18 <= tempExt <= 24:
                if comfort == 0:
                    return 81
                if comfort == 1:
                    return 82
                if comfort == 2:
                    return 83
            if 24 < tempExt <= 29:
                if comfort == 0:
                    return 84
                if comfort == 1:
                    return 85
                if comfort == 2:
                    return 86
            if 29 < tempExt <= 35:
                if comfort == 0:
                    return 87
                if comfort == 1:
                    return 88
                if comfort == 2:
                    return 89
        if 6 <= ac_status <= 8:  # [19,21]
            if 18 <= tempExt <= 24:
                if comfort == 0:
                    return 90
                if comfort == 1:
                    return 91
                if comfort == 2:
                    return 92
            if 24 < tempExt <= 29:
                if comfort == 0:
                    return 93
                if comfort == 1:
                    return 94
                if comfort == 2:
                    return 95
            if 29 < tempExt <= 35:
                if comfort == 0:
                    return 96
                if comfort == 1:
                    return 97
                if comfort == 2:
                    return 98
        if 9 <= ac_status <= 11:  # [22,24]
            if 18 <= tempExt <= 24:
                if comfort == 0:
                    return 99
                if comfort == 1:
                    return 100
                if comfort == 2:
                    return 101
            if 24 < tempExt <= 29:
                if comfort == 0:
                    return 102
                if comfort == 1:
                    return 103
                if comfort == 2:
                    return 104
            if 29 < tempExt <= 35:
                if comfort == 0:
                    return 105
                if comfort == 1:
                    return 106
                if comfort == 2:
                    return 107


def get_next_state(current_state: int, action: int) -> int:
    """
        las acciones son 0: apagar, 1: subir, 2: bajar;
        los estados son 0,,108
    """
    if action == 0:
        # p1 - off
        if current_state == 0:
            return 0
        if current_state == 1:
            return 1
        if current_state == 2:
            return 2
        if current_state == 3:
            return 3
        if current_state == 4:
            return 4
        if current_state == 5:
            return 5
        if current_state == 6:
            return 6
        if current_state == 7:
            return 7
        if current_state == 8:
            return 8
        # p1 - t1
        if current_state == 9:
            return 0
        if current_state == 10:
            return 1
        if current_state == 11:
            return 2
        if current_state == 12:
            return 3
        if current_state == 13:
            return 4
        if current_state == 14:
            return 5
        if current_state == 15:
            return 6
        if current_state == 16:
            return 7
        if current_state == 17:
            return 8
        # p1 - t2
        if current_state == 18:
            return 0
        if current_state == 19:
            return 1
        if current_state == 20:
            return 2
        if current_state == 21:
            return 3
        if current_state == 22:
            return 4
        if current_state == 23:
            return 5
        if current_state == 24:
            return 6
        if current_state == 25:
            return 7
        if current_state == 26:
            return 8
        # p1 - t3
        if current_state == 27:
            return 0
        if current_state == 28:
            return 1
        if current_state == 29:
            return 2
        if current_state == 30:
            return 3
        if current_state == 31:
            return 4
        if current_state == 32:
            return 5
        if current_state == 33:
            return 6
        if current_state == 34:
            return 7
        if current_state == 35:
            return 8
        # p2 - off
        if current_state == 36:
            return 36
        if current_state == 37:
            return 37
        if current_state == 38:
            return 38
        if current_state == 39:
            return 39
        if current_state == 40:
            return 40
        if current_state == 41:
            return 41
        if current_state == 42:
            return 42
        if current_state == 43:
            return 43
        if current_state == 44:
            return 44
        # p2 - t1
        if current_state == 45:
            return 36
        if current_state == 46:
            return 37
        if current_state == 47:
            return 38
        if current_state == 48:
            return 39
        if current_state == 49:
            return 40
        if current_state == 50:
            return 41
        if current_state == 51:
            return 42
        if current_state == 52:
            return 43
        if current_state == 53:
            return 44
        # p2 -t2
        if current_state == 54:
            return 36
        if current_state == 55:
            return 37
        if current_state == 56:
            return 38
        if current_state == 57:
            return 39
        if current_state == 58:
            return 40
        if current_state == 59:
            return 41
        if current_state == 60:
            return 42
        if current_state == 61:
            return 43
        if current_state == 62:
            return 44
        # p2 - t3
        if current_state == 63:
            return 36
        if current_state == 64:
            return 37
        if current_state == 65:
            return 38
        if current_state == 66:
            return 39
        if current_state == 67:
            return 40
        if current_state == 68:
            return 41
        if current_state == 69:
            return 42
        if current_state == 70:
            return 43
        if current_state == 71:
            return 44
        # p3 - off
        if current_state == 72:
            return 72
        if current_state == 73:
            return 73
        if current_state == 74:
            return 74
        if current_state == 75:
            return 75
        if current_state == 76:
            return 76
        if current_state == 77:
            return 77
        if current_state == 78:
            return 78
        if current_state == 79:
            return 79
        if current_state == 80:
            return 80
        # p3 - t1
        if current_state == 81:
            return 72
        if current_state == 82:
            return 73
        if current_state == 83:
            return 74
        if current_state == 84:
            return 75
        if current_state == 85:
            return 76
        if current_state == 86:
            return 77
        if current_state == 87:
            return 78
        if current_state == 88:
            return 79
        if current_state == 89:
            return 80

        # p3 - t2
        if current_state == 90:
            return 72
        if current_state == 91:
            return 73
        if current_state == 92:
            return 74
        if current_state == 93:
            return 75
        if current_state == 94:
            return 76
        if current_state == 95:
            return 77
        if current_state == 96:
            return 78
        if current_state == 97:
            return 79
        if current_state == 98:
            return 80

        # p3 - t3
        if current_state == 99:
            return 72
        if current_state == 100:
            return 73
        if current_state == 101:
            return 74
        if current_state == 102:
            return 75
        if current_state == 103:
            return 76
        if current_state == 104:
            return 77
        if current_state == 105:
            return 78
        if current_state == 106:
            return 79
        if current_state == 107:
            return 80

    if action == 1:
        # p1 - off
        if current_state == 0:
            return 27
        if current_state == 1:
            return 28
        if current_state == 2:
            return 29
        if current_state == 3:
            return 30
        if current_state == 4:
            return 31
        if current_state == 5:
            return 32
        if current_state == 6:
            return 33
        if current_state == 7:
            return 34
        if current_state == 8:
            return 35
        # p1 - t1
        if current_state == 9:
            return 18
        if current_state == 10:
            return 19
        if current_state == 11:
            return 20
        if current_state == 12:
            return 21
        if current_state == 13:
            return 22
        if current_state == 14:
            return 23
        if current_state == 15:
            return 24
        if current_state == 16:
            return 25
        if current_state == 17:
            return 26
        # p1 - t2
        if current_state == 18:
            return 27
        if current_state == 19:
            return 28
        if current_state == 20:
            return 29
        if current_state == 21:
            return 30
        if current_state == 22:
            return 31
        if current_state == 23:
            return 32
        if current_state == 24:
            return 33
        if current_state == 25:
            return 34
        if current_state == 26:
            return 35
        # p1 - t3
        if current_state == 27:
            return 27
        if current_state == 28:
            return 28
        if current_state == 29:
            return 29
        if current_state == 30:
            return 30
        if current_state == 31:
            return 31
        if current_state == 32:
            return 32
        if current_state == 33:
            return 33
        if current_state == 34:
            return 34
        if current_state == 35:
            return 35
        # p2 - off
        if current_state == 36:
            return 63
        if current_state == 37:
            return 64
        if current_state == 38:
            return 65
        if current_state == 39:
            return 66
        if current_state == 40:
            return 67
        if current_state == 41:
            return 68
        if current_state == 42:
            return 69
        if current_state == 43:
            return 70
        if current_state == 44:
            return 71
        # p2 - t1
        if current_state == 45:
            return 54
        if current_state == 46:
            return 55
        if current_state == 47:
            return 56
        if current_state == 48:
            return 57
        if current_state == 49:
            return 58
        if current_state == 50:
            return 59
        if current_state == 51:
            return 60
        if current_state == 52:
            return 61
        if current_state == 53:
            return 62
        # p2 -t2
        if current_state == 54:
            return 63
        if current_state == 55:
            return 64
        if current_state == 56:
            return 65
        if current_state == 57:
            return 66
        if current_state == 58:
            return 67
        if current_state == 59:
            return 68
        if current_state == 60:
            return 69
        if current_state == 61:
            return 70
        if current_state == 62:
            return 71
        # p2 - t3
        if current_state == 63:
            return 63
        if current_state == 64:
            return 64
        if current_state == 65:
            return 65
        if current_state == 66:
            return 66
        if current_state == 67:
            return 67
        if current_state == 68:
            return 68
        if current_state == 69:
            return 69
        if current_state == 70:
            return 70
        if current_state == 71:
            return 71
        # p3 - off
        if current_state == 72:
            return 99
        if current_state == 73:
            return 100
        if current_state == 74:
            return 101
        if current_state == 75:
            return 102
        if current_state == 76:
            return 103
        if current_state == 77:
            return 104
        if current_state == 78:
            return 105
        if current_state == 79:
            return 106
        if current_state == 80:
            return 107
        # p3 - t1
        if current_state == 81:
            return 90
        if current_state == 82:
            return 91
        if current_state == 83:
            return 92
        if current_state == 84:
            return 93
        if current_state == 85:
            return 94
        if current_state == 86:
            return 95
        if current_state == 87:
            return 96
        if current_state == 88:
            return 97
        if current_state == 89:
            return 98

        # p3 - t2
        if current_state == 90:
            return 99
        if current_state == 91:
            return 100
        if current_state == 92:
            return 101
        if current_state == 93:
            return 102
        if current_state == 94:
            return 103
        if current_state == 95:
            return 104
        if current_state == 96:
            return 105
        if current_state == 97:
            return 106
        if current_state == 98:
            return 107

        # p3 - t3
        if current_state == 99:
            return 99
        if current_state == 100:
            return 100
        if current_state == 101:
            return 101
        if current_state == 102:
            return 102
        if current_state == 103:
            return 103
        if current_state == 104:
            return 104
        if current_state == 105:
            return 105
        if current_state == 106:
            return 106
        if current_state == 107:
            return 107

    if action == 2:
        # p1 - off
        if current_state == 0:
            return 0
        if current_state == 1:
            return 1
        if current_state == 2:
            return 2
        if current_state == 3:
            return 3
        if current_state == 4:
            return 4
        if current_state == 5:
            return 5
        if current_state == 6:
            return 6
        if current_state == 7:
            return 7
        if current_state == 8:
            return 8
        # p1 - t1
        if current_state == 9:
            return 9
        if current_state == 10:
            return 10
        if current_state == 11:
            return 11
        if current_state == 12:
            return 12
        if current_state == 13:
            return 13
        if current_state == 14:
            return 14
        if current_state == 15:
            return 15
        if current_state == 16:
            return 16
        if current_state == 17:
            return 17
        # p1 - t2
        if current_state == 18:
            return 9
        if current_state == 19:
            return 10
        if current_state == 20:
            return 11
        if current_state == 21:
            return 12
        if current_state == 22:
            return 13
        if current_state == 23:
            return 14
        if current_state == 24:
            return 15
        if current_state == 25:
            return 16
        if current_state == 26:
            return 17
        # p1 - t3
        if current_state == 27:
            return 18
        if current_state == 28:
            return 19
        if current_state == 29:
            return 20
        if current_state == 30:
            return 21
        if current_state == 31:
            return 22
        if current_state == 32:
            return 23
        if current_state == 33:
            return 24
        if current_state == 34:
            return 25
        if current_state == 35:
            return 26
        # p2 - off
        if current_state == 36:
            return 36
        if current_state == 37:
            return 37
        if current_state == 38:
            return 38
        if current_state == 39:
            return 39
        if current_state == 40:
            return 40
        if current_state == 41:
            return 41
        if current_state == 42:
            return 42
        if current_state == 43:
            return 43
        if current_state == 44:
            return 44
        # p2 - t1
        if current_state == 45:
            return 45
        if current_state == 46:
            return 46
        if current_state == 47:
            return 47
        if current_state == 48:
            return 48
        if current_state == 49:
            return 49
        if current_state == 50:
            return 50
        if current_state == 51:
            return 51
        if current_state == 52:
            return 52
        if current_state == 53:
            return 53
        # p2 -t2
        if current_state == 54:
            return 45
        if current_state == 55:
            return 46
        if current_state == 56:
            return 47
        if current_state == 57:
            return 48
        if current_state == 58:
            return 49
        if current_state == 59:
            return 50
        if current_state == 60:
            return 51
        if current_state == 61:
            return 52
        if current_state == 62:
            return 53
        # p2 - t3
        if current_state == 63:
            return 54
        if current_state == 64:
            return 55
        if current_state == 65:
            return 56
        if current_state == 66:
            return 57
        if current_state == 67:
            return 58
        if current_state == 68:
            return 59
        if current_state == 69:
            return 60
        if current_state == 70:
            return 61
        if current_state == 71:
            return 62
        # p3 - off
        if current_state == 72:
            return 72
        if current_state == 73:
            return 73
        if current_state == 74:
            return 74
        if current_state == 75:
            return 75
        if current_state == 76:
            return 76
        if current_state == 77:
            return 77
        if current_state == 78:
            return 78
        if current_state == 79:
            return 79
        if current_state == 80:
            return 80
        # p3 - t1
        if current_state == 81:
            return 81
        if current_state == 82:
            return 82
        if current_state == 83:
            return 83
        if current_state == 84:
            return 84
        if current_state == 85:
            return 85
        if current_state == 86:
            return 86
        if current_state == 87:
            return 87
        if current_state == 88:
            return 88
        if current_state == 89:
            return 89

        # p3 - t2
        if current_state == 90:
            return 81
        if current_state == 91:
            return 82
        if current_state == 92:
            return 83
        if current_state == 93:
            return 84
        if current_state == 94:
            return 85
        if current_state == 95:
            return 86
        if current_state == 96:
            return 87
        if current_state == 97:
            return 88
        if current_state == 98:
            return 89

        # p3 - t3
        if current_state == 99:
            return 90
        if current_state == 100:
            return 91
        if current_state == 101:
            return 92
        if current_state == 102:
            return 93
        if current_state == 103:
            return 94
        if current_state == 104:
            return 95
        if current_state == 105:
            return 96
        if current_state == 106:
            return 97
        if current_state == 107:
            return 98
