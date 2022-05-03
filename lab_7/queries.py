in_this_week_query = f"""
    SELECT day, start_time, name, room_numb, full_name
    FROM timetable
    JOIN subject ON timetable.subject_id = subject.id
    JOIN teacher ON subject.id = teacher.subject_id
    WHERE day >= %s AND day <= %s
    ORDER BY day, start_time;
"""

on_day_of_week = f"""
    SELECT day, start_time, name, room_numb, full_name
    FROM timetable
    JOIN subject ON timetable.subject_id = subject.id
    JOIN teacher ON subject.id = teacher.subject_id
    WHERE day = %s
    ORDER BY day, start_time;
"""
