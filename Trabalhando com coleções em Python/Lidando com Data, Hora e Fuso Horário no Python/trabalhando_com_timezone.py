# pip install pytz

import datetime
import pytz

#  Com pytz

# Criando datetime com timezone de São Paulo
tz_sao_paulo = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))

print(f'''====== TIME ZONE ======
Timezone São Paulo: {tz_sao_paulo}''')

# Lista de 12 timezones diferentes
timezones = [
    "America/New_York",
    "Europe/London",
    "Europe/Paris",
    "Asia/Tokyo",
    "Australia/Sydney",
    "Asia/Dubai",
    "America/Los_Angeles",
    "Asia/Shanghai",
    "Africa/Johannesburg",
    "America/Argentina/Buenos_Aires",
    "Europe/Moscow",
    "Pacific/Auckland",
]

print("\n====== OUTRAS TIMEZONES ======")
for tz_name in timezones:
    timezone = pytz.timezone(tz_name)
    now_in_tz = datetime.datetime.now(timezone)
    print(f"{tz_name}: {now_in_tz}")

print("\n====== OUTRAS TIMEZONES (COMPARADO COM UTC) ======")
for tz_name in timezones:
    timezone = pytz.timezone(tz_name)
    now_in_tz = datetime.datetime.now(timezone)
    utc_offset = now_in_tz.utcoffset()
    print(f"{tz_name}: {now_in_tz} (UTC{'+' if utc_offset.total_seconds() >= 0 else ''}{utc_offset})")

# Com timezone utc

tz_sao_paulo_utc = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2)))

print(f'''
====== TIME ZONE ======
Timezone São Paulo com UTC: {tz_sao_paulo}''')