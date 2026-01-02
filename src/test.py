import re
import json

def parse_recaps(input_string):
    pattern = re.compile(
        r'<a\s+href="([^"]+)"[^>]*>\s*([\d\-]+):\s*(.*?)\s*</a>',
        re.IGNORECASE
    )

    results = []

    matches = pattern.findall(input_string)
    for recap_url, date, name in matches:
        results.append({
            "name": name,
            "date": date,
            "recap": recap_url
        })

    return json.dumps(results)

import json

def transform_events(input_string):
    # Parse the input JSON string into Python objects
    data = json.loads(input_string)

    result = {}

    for item in data:
        name = item.get("name")
        result[name] = {
            "date": item.get("date"),
            "recap": item.get("recap")
        }

    # Return the result as a JSON string
    return json.dumps(result)

input2 = """
[
  {"date": "2-01-20", "recap": "https://docs.google.com/document/d/1NY7k5ZdvMczqQ2cToR47BTQnS27GM3610PHW8iY0lZQ/edit?usp=sharing", "name": "Boardwalk Hall"}, 
  {"date": "6-16-20", "recap": "https://docs.google.com/document/d/1gJqvKgNog4KVhEHmJIVhhf8GCnKOm2ZCXYQ2H7nIzM4/edit?usp=sharing", "name": "Paragon Speedway"}, 
  {"date": "6-19-20", "recap": "https://docs.google.com/document/d/1NlYWfZVLht_UwNYtHa-7p65voO4GlXjnLxh_KkK_o0Y/edit?usp=sharing", "name": "Tri-State Speedway"}, 
  {"date": "7-03-20", "recap": "https://docs.google.com/document/d/14xdSQpGZenzPFbWwTEVv66lM-tgusrEKlxeOzbX8KAc/edit?usp=sharing", "name": "Big Diamond Speedway"}, 
  {"date": "7-04-20", "recap": "https://docs.google.com/document/d/1EtTQTugt0_Mw0hXvZv4SdsHsy1e1tujFf634Inm-Gbk/edit?usp=sharing", "name": "White Mountain Motorsports Park"}, 
  {"date": "8-01-20", "recap": "https://docs.google.com/document/d/1KKiLqBxGqsEDS_sP7dcQN1SXmfaA8WSqDSZUwHnrrKU/edit?usp=sharing", "name": "Londonderry Raceway"}, 
  {"date": "8-21-20", "recap": "https://docs.google.com/document/d/1Wuo6WNWFi39lUxDThPQvvv7ClVCO-ZO4-R_6kaOrqtQ/edit?usp=sharing", "name": "Lucas Oil Raceway"}, 
  {"date": "8-23-20", "recap": "https://docs.google.com/document/d/1JOzXzV5dWs1pkkGUJ49p91UnN6FlQxi4uoikMSOGMJ8/edit?usp=sharing", "name": "Indiana State Fairgrounds"}, 
  {"date": "9-12-20", "recap": "https://docs.google.com/document/d/10wz-9ODQhCdf-G2QdlYHLyQeKkfXIv21mjsZLRs3I5E/edit?usp=sharing", "name": "New Hampshire Motor Speedway Legends Oval"}, 
  {"date": "1-31-21", "recap": "https://docs.google.com/document/d/1kJyQOA3ces6SEA0JNmJFrRRRFzPVcvQXpkavjmmTXwo/edit?usp=sharing", "name": "Lee Pond"}, 
  {"date": "3-06-21", "recap": "https://docs.google.com/document/d/1uVg5Ohk6ZKgTdaSJPtomYtPOFiLyU-G4YZvrrf6t4ns/edit?usp=sharing", "name": "Rochester Fairgrounds"}, 
  {"date": "3-26-21", "recap": "https://docs.google.com/document/d/1Cmbm8ZPXGMjbTYtg4OoMB3Vfv3in7nth9t_QcwScQXM/edit?usp=sharing", "name": "Boyd's Speedway"}, 
  {"date": "5-08-21", "recap": "https://docs.google.com/document/d/1T9WVdlRPcuie9G1TApOcL0QG7V-lp214QGvxcjISZIA/edit?usp=sharing", "name": "Rochester Fairgrounds (Road Course)"}, 
  {"date": "5-23-21", "recap": "https://docs.google.com/document/d/1HUCtDeaBU6EZqZF5RCsLEatfio0AZBndus-wy8dHusA/edit?usp=sharing", "name": "Central Cycle Club"}, 
  {"date": "5-23-21", "recap": "https://docs.google.com/document/d/1_x7UtZxyb2uPf17I-WoQkrFZh73FCOoYA7Gz7Lx0GsE/edit?usp=sharing", "name": "Pomfret Speedway"}, 
  {"date": "5-29-21", "recap": "https://docs.google.com/document/d/1cF1Y-QeVOz6HNsb2F7ymF72NLLy-HOlkNfqwg1GJojo/edit?usp=sharing", "name": "Fulton Speedway"}, 
  {"date": "6-13-21", "recap": "https://docs.google.com/document/d/1-Bf2hFWNjW1brrH5yBAPVWeKA0QTLsx2fOsQgyb3vm0/edit?usp=sharing", "name": "Action Track USA"}, 
  {"date": "6-14-21", "recap": "https://docs.google.com/document/d/1jMUlM44lKosb2e5Hw0G9kQUYg1-auFUfvk_7tvORAOA/edit?usp=sharing", "name": "Wayne County Speedway"}, 
  {"date": "6-19-21", "recap": "https://docs.google.com/document/d/1-vJNUO0HReic3QRckm27whW_tLF75LkzIZedVp7q_RA/edit?usp=sharing", "name": "Path Valley Speedway Park"}, 
  {"date": "6-20-21", "recap": "https://docs.google.com/document/d/1dlKKKhfcHdsTPexN3efjKSq_kEe_Zu3YKMd8wfZgLGE/edit?usp=sharing", "name": "Selinsgrove Raceway Park"}, 
  {"date": "6-20-21", "recap": "https://docs.google.com/document/d/1qY46UKPuyo0DyH03f1_4N_Ka2MP-zQjDmM0QrTOCIGA/edit?usp=sharing", "name": "Bloomsburg Fair Speedway"}, 
  {"date": "6-26-21", "recap": "https://docs.google.com/document/d/1fZmpM_dK53k1XD1uFWTdK87kTXnH60bJWJQ1KpXhJn0/edit?usp=sharing", "name": "Riverhead Raceway"}, 
  {"date": "7-08-21", "recap": "https://docs.google.com/document/d/1CY-ep1JF6d2orvtvh8oz6gaQorIfsBWFIptMfS8jFy0/edit?usp=sharing", "name": "KRA Speedway"}, 
  {"date": "7-10-21", "recap": "https://docs.google.com/document/d/1Bw1HcyUPJwhMolZsvYC8JkvQE9ry6WTudaRjuPkL5og/edit?usp=sharing", "name": "ERX Motor Park"}, 
  {"date": "8-21-21", "recap": "https://docs.google.com/document/d/1btVwp8LM-6Q4S8tPVAzdLTsVzynMoD8EcI2G_ENPIzk/edit?usp=sharing", "name": "Perris Auto Speedway"}, 
  {"date": "9-10-21", "recap": "https://docs.google.com/document/d/1u_Mx9-J5ApGQ3x6562fa1teoJuRYLDARj7_DuB2C1QQ/edit?usp=sharing", "name": "Huset's Speedway"}, 
  {"date": "10-02-21", "recap": "https://docs.google.com/document/d/1k68ABZnlcbOm8ZzaRrAXJVTcJh4_UO08KvfKjYKqXnA/edit?usp=sharing", "name": "Talladega Superspeedway"}, 
  {"date": "10-02-21", "recap": "https://docs.google.com/document/d/1SxHar13_X1DDIvXW8uDMHoM6nDsolFXN0PLk-rxPBnM/edit?usp=sharing", "name": "Talladega Short Track"}, 
  {"date": "10-11-21", "recap": "https://docs.google.com/document/d/15KjPfsdFj6AHZXhDFu9egy4Gt481T7A5chQIAk83zm0/edit?usp=sharing", "name": "Topsfield Fair"}, 
  {"date": "11-12-21", "recap": "https://docs.google.com/document/d/1YszGHme3-q9X9SgUYqWXc-VyEhS8B9BHQHODCDXCOpI/edit?usp=sharing", "name": "Arizona Speedway"}, 
  {"date": "11-20-21", "recap": "https://docs.google.com/document/d/1Z5YTOHT81HoclolnJAomHC3hgmE-L-iP5sPPlyTBRCY/edit?usp=sharing", "name": "Perris Auto Speedway (Figure-8, Inner Oval, Road Course)"}, 
  {"date": "1-27-22", "recap": "https://docs.google.com/document/d/1vSoctG7H6KN6MjDYqTSBwHF6pm314P0HVKKk7qUYgIc/edit?usp=sharing", "name": "Cocopah Speedway"}, 
  {"date": "2-05-22", "recap": "https://docs.google.com/document/d/1BCBJbbBOcCUcQgaYMhX10NafgDVv1zVkEZmHhV2zGog/edit?usp=sharing", "name": "Irwindale Speedway"}, 
  {"date": "2-06-22", "recap": "https://docs.google.com/document/d/17I03RuIsZzwAsp66-2LxH3i5DBYn1H2xigY53PsEtgU/edit?usp=sharing", "name": "Los Angeles Memorial Colisum"}, 
  {"date": "3-18-22", "recap": "https://docs.google.com/document/d/1_iSHK60CfFMC6qBIbdU9P5RqFcJO79D3imj_70SrnI0/edit?usp=sharing", "name": "Hickory Motor Speedway"}, 
  {"date": "3-18-22", "recap": "https://docs.google.com/document/d/1_fSjP3YH0T0ZWSLWAwYl-_WzgHDXrOeDf5coCBdODT4/edit?usp=sharing", "name": "Carolina Speedway"}, 
  {"date": "3-26-22", "recap": "https://docs.google.com/document/d/1Dc-XE-gm02P41M8cX6vA24AnJEZW0n-W85eq0u2WIHs/edit?usp=sharing", "name": "Cherokee Speedway"}, 
  {"date": "6-11-22", "recap": "https://docs.google.com/document/d/1AhQjZiDoXSCiT0CZoTgtPYhdnFKdi3lKZR9ijobAsmo/edit?usp=sharing", "name": "Ventura Raceway"}, 
  {"date": "6-18-22", "recap": "https://docs.google.com/document/d/1fdsuRQeIrU5tNUQtGvzzaimkmG68T7fQcQI05-peTks/edit?usp=sharing", "name": "Bakersfield Speedway (Inner)"}, 
  {"date": "6-18-22", "recap": "https://docs.google.com/document/d/1TArP-p33CCSbzo5fjXRD0T1sd_O_NqK-HEMaGUBSv1A/edit?usp=sharing", "name": "Kern County Raceway (Asphalt))"}, 
  {"date": "6-23-22", "recap": "https://docs.google.com/document/d/1OOLMCagoDsybCN9Lwl4WEODLKFUWR9VDToevCP7Z0KQ/edit?usp=sharing", "name": "Skagit Speedway"}, 
  {"date": "7-18-22", "recap": "https://docs.google.com/document/d/1M2-FOnTfNowCwr3cCR_S-gr09tc4T5tu27oJBRSG3c4/edit?usp=sharing", "name": "Greenwood Valley Action Tracks"}, 
  {"date": "7-21-22", "recap": "https://docs.google.com/document/d/1n_uz8ccI1RqW51nEa1yFo05IqQ-LKf4r3Sual1ARnGo/edit?usp=sharing", "name": "Linda's Speedway"}, 
  {"date": "7-25-22", "recap": "https://docs.google.com/document/d/1Bg6ST4Wqj-r7WkhBVXdIokKVgRcMAwfej6nX9S2EzwY/edit?usp=sharing", "name": "Circle City Raceway"}, 
  {"date": "7-27-22", "recap": "https://docs.google.com/document/d/1Q4Kmi7RdIEinGkxn1jvn6Jomy1lUfOyyzJ2hRytx8jM/edit?usp=sharing", "name": "Pendleton County Fairgrounds"}, 
  {"date": "7-29-22", "recap": "https://docs.google.com/document/d/19qrE3wIL4vhjl24sH96GAa_CfKitODL1s-zrG_wJRwg/edit?usp=sharing", "name": "Bloomington Speedway"}, 
  {"date": "7-31-22", "recap": "https://docs.google.com/document/d/1R1PeRd2QQ5ANKIBhwL4OedMQxyHqZdvNpeaBZjnyQCE/edit?usp=sharing", "name": "Dirt City Motorplex"}, 
  {"date": "8-14-22", "recap": "https://docs.google.com/document/d/1O0yxPre_MK0auw3uxa2OIjKdp69heqw1tejIMViVDtQ/edit?usp=sharing", "name": "New Hampshire Motor Speedway Road Course (Full)"}, 
  {"date": "8-19-22", "recap": "https://docs.google.com/document/d/1Dkty51LP-qxLMXsT2U_FhX2T8cRTEwp7954tpHIxHI8/edit?usp=sharing", "name": "Outlaw Speedway"}, 
  {"date": "8-20-22", "recap": "https://docs.google.com/document/d/1Gp0Igi_6eBAcVrAK14o3o1gXzBgVfcpGZaYB6ZVv1e4/edit?usp=sharing", "name": "Skyline Raceway Motorsports Park"}, 
  {"date": "8-20-22", "recap": "https://docs.google.com/document/d/1fVZBEgPEHSrMXNTERhDK1Oot035Ub4Bh12jOYCu-d3Y/edit?usp=sharing", "name": "Five Mile Point Speedway"}, 
  {"date": "9-30-22", "recap": "https://docs.google.com/document/d/1m6lw-P_mLKPR1nfu1CUmHMpi_v0etaT7i4W1FB-QmuA/edit?usp=sharing", "name": "I-30 Speedway"}, 
  {"date": "10-06-22", "recap": "https://docs.google.com/document/d/1xgMoNdnybQSwvDL_0o7EeMXmyXNk3jOkvV5gnrdBgmc/edit?usp=sharing", "name": "Tri-County Racetrack"}, 
  {"date": "10-08-22", "recap": "https://docs.google.com/document/d/1a1ejb20ge3ksqiHRKJCawQjEbOA1wAJDiS_HnF79F30/edit?usp=sharing", "name": "Nashville Fairgrounds Speedway (Inner)"}, 
  {"date": "10-11-22", "recap": "https://docs.google.com/document/d/11Ofpyvo46MBpJd3JB4mHhmSAFn2gyAkQ5zTYofvLyxM/edit?usp=sharing", "name": "411 Motor Speedway"}, 
  {"date": "11-12-22", "recap": "https://docs.google.com/document/d/1NmgNoN75-Tjb9U5RTKs1Au20t5tE-SLKBPNuO6YroD0/edit?usp=sharing", "name": "Adobe Mountain Speedway"}, 
  {"date": "11-15-22", "recap": "https://docs.google.com/document/d/11SfqzFBMiZeI6gk4UmyAKP8e-uqcrnQQn-JY5ueK-zU/edit?usp=sharing", "name": "Bakersfield Speedway"}, 
  {"date": "12-17-22", "recap": "https://docs.google.com/document/d/1rIIH_l2GhHZKOUQ9azU08F6W3yobhEx9rymBFkw3Qo4/edit?usp=sharing", "name": "Southern Illinois Center"}, 
  {"date": "1-21-23", "recap": "https://docs.google.com/document/d/14QvuES0oEQNPas13F_ZV_cfFX4ILCbfK-EQO7zk7R_4/edit?usp=sharing", "name": "Circuit de Trois Rivieres Rallycross"}, 
  {"date": "2-09-23", "recap": "https://docs.google.com/document/d/1_i7Xw_zy7f7xMOrwF7dGHwNEux-OeH8Fm3JuIOReGFQ/edit?usp=sharing", "name": "Volusia Speedway Park"}, 
  {"date": "2-10-23", "recap": "https://docs.google.com/document/d/11Pg9Z2GVXR79qUS-Jgw_jtbg15mQjyd1rUswv4VlbUE/edit?usp=sharing", "name": "Auburndale Speedway"}, 
  {"date": "2-10-23", "recap": "https://docs.google.com/document/d/1ro6-p7BEPoCU8hcNU8xZKW8pMEXMcoPhJ4u16U5-FkM/edit?usp=sharing", "name": "Showtime Speedway (Oval and Figure-8)"}, 
  {"date": "2-11-23", "recap": "https://docs.google.com/document/d/1UWfVlUCVHohfQSZLCLWHJRYP3efzYdsMATXerDVUeps/edit?usp=sharing", "name": "Hobe Sound Speedway"}, 
  {"date": "2-11-23", "recap": "https://docs.google.com/document/d/1mvRNAsOzxlIovYom9Or6aaYuKKye5pneYkwksTQA4xw/edit?usp=sharing", "name": "Hendry County Motorsports Park"}, 
  {"date": "2-12-23", "recap": "https://docs.google.com/document/d/1w8WcgOkN906qGp78tAyxHIjRhOw6TCx21Xc3TtJA6Yo/edit?usp=sharing", "name": "New Smyrna Speedway"}, 
  {"date": "2-13-23", "recap": "https://docs.google.com/document/d/1IkljAMfplrLVPvEldvDBVEGDjYRgCbS8Uinqc8LHyjM/edit?usp=sharing", "name": "East Bay Raceway Park"}, 
  {"date": "2-16-23", "recap": "https://docs.google.com/document/d/1YJpOtM7ofRdTjp9jpDUiGzxT8rAzcs3lEqGjKdkDZsI/edit?usp=sharing", "name": "Citrus County Speedway"}, 
  {"date": "2-16-23", "recap": "https://docs.google.com/document/d/1a5FV--NhwjTZ_mAuqKYkQigWjme6qbsyx88P727_Yjw/edit?usp=sharing", "name": "Bubba Raceway Park"}, 
  {"date": "5-19-23", "recap": "https://docs.google.com/document/d/13gPGQCSHwjn-2hagP2YMB0V3OEwPItnYlj1e0XO7yBs/edit?usp=sharing", "name": "Clinton County Speedway"}, 
  {"date": "5-20-23", "recap": "https://docs.google.com/document/d/1P5K6V0GQtRodNLoMcysHIMsp65WHYvH9G8cmuhTAUTA/edit?usp=sharing", "name": "Bowman Gray Stadium"}, 
  {"date": "5-28-23", "recap": "https://docs.google.com/document/d/1MRi774EQu4-RPp9-cxXbfeac35L2PR85CfQ8AIfgxGY/edit?usp=sharing", "name": "Wiscasset Speedway"}, 
  {"date": "7-02-23", "recap": "https://docs.google.com/document/d/1xRaCTrM6tAow4wu7A8P86p4dbxwptctXe3uQsVS4sFs/edit?usp=sharing", "name": "Chicago Street Course"}, 
  {"date": "7-03-23", "recap": "https://docs.google.com/document/d/1FXwlH6jL0VPuczJj_0IkkHdZnRen8j9fgXg5ck8VPAU/edit?usp=sharing", "name": "Rockford Speedway"}, 
  {"date": "7-04-23", "recap": "https://docs.google.com/document/d/17oZDDJ7k__B2dWp35OGNjrQp-1AbMpg6n4xZav2WCgQ/edit?usp=sharing", "name": "What Cheer Raceway"}, 
  {"date": "7-05-23", "recap": "https://docs.google.com/document/d/1gAqlMxUiyNDHWiktJZDbmtV5DB8nOVgEqG-R7Zbqf94/edit?usp=sharing", "name": "Independence Motor Speedway"}, 
  {"date": "7-07-23", "recap": "https://docs.google.com/document/d/1WFw_Q2LbU7oZRxO8ssiYaj0DFGiS-xPheVrhpwlTGtg/edit?usp=sharing", "name": "Farmer City Raceway"}, 
  {"date": "7-15-23", "recap": "https://docs.google.com/document/d/1T6lqbapYMhBwThFdZTxuiV0bz3mYv58mLlij2WZMK68/edit?usp=sharing", "name": "NHMX Flat Track"}, 
  {"date": "7-23-23", "recap": "https://docs.google.com/document/d/1Ayg89A_o3pJUCjYky7f8ThbUMnmLevr8wVP6Ipp1NE0/edit?usp=sharing", "name": "Pocono Raceway"}, 
  {"date": "8-12-23", "recap": "https://docs.google.com/document/d/1kk1dKll-L6jv1WGo9N3t4tnk0-DRSEHL674_ZmX_o5c/edit?usp=sharing", "name": "Winchester Speedway"}, 
  {"date": "8-26-23", "recap": "https://docs.google.com/document/d/1Je4ZTS-7hgr2dPM123eBsJ3S2kt7KvQfsTsFFqknkxQ/edit?usp=sharing", "name": "Marshfield Fair"}, 
  {"date": "9-29-23", "recap": "https://docs.google.com/document/d/1dHYUgXgJasMN9YRgKtZr5x8RLhXs4dyErkEbRibCjdw/edit?usp=sharing", "name": "Unity Raceway"}, 
  {"date": "9-30-23", "recap": "https://docs.google.com/document/d/1MlBEpqJr69vPNIy5vSUZiE40QnWz9xeWyPpSCkTwxYU/edit?usp=sharing", "name": "Thompson Speedway (Asphalt Road Course)"}, 
  {"date": "10-20-23", "recap": "https://docs.google.com/document/d/11pgOum_uPd6dvrBMGz-dA3c2O2FKq9BLFV08oN2fbuI/edit?usp=sharing", "name": "Devil's Bowl Speedway (TX)"}, 
  {"date": "11-04-23", "recap": "https://docs.google.com/document/d/13NEjgH_MhmIjhm5JAzo-lnBKtliHMG5Gvd4F4CNmX1Q/edit?usp=sharing", "name": "Stockton Dirt Track"}, 
  {"date": "11-05-23", "recap": "https://docs.google.com/document/d/1TmZPUVQiXJA85dInqKaIPd_mjZDgwwlOKSqblb75NlA/edit?usp=sharing", "name": "SBC Fairgrounds"}, 
  {"date": "11-10-23", "recap": "https://docs.google.com/document/d/1D1uQOG7PMklUKOL1BOUZl9GPjVte7N1DRCAbVQQ9UWo/edit?usp=sharing", "name": "Central Arizona Raceway"}, 
  {"date": "11-11-23", "recap": "https://docs.google.com/document/d/1re-5NPavMWakhjQsAAXrgWLP4LW_BvTrdzNKCrhzaN4/edit?usp=sharing", "name": "Podium Club at Attesa (Full Course)"}, 
  {"date": "11-12-23", "recap": "https://docs.google.com/document/d/1kZgS1EOsRGdaSLQsawPjQ1j1Grr3kr9P6B-H0B3QlWE/edit?usp=sharing", "name": "Shorty's Sports Park"}, 
  {"date": "11-17-23", "recap": "https://docs.google.com/document/d/1-74uKcHC0Px-KrsNWaVaAkV2LkO4s_-Ve-sp6vNnEoA/edit?usp=sharing", "name": "Placerville Speedway"}, 
  {"date": "11-21-23", "recap": "https://docs.google.com/document/d/1aX8mYQEKPC9OhaaoGxTfESQN67wknyB2yakUWw_fv7A/edit?usp=sharing", "name": "Merced Speedway"}, 
  {"date": "12-01-23", "recap": "https://docs.google.com/document/d/1eHpzJxAEA7KSw74zOtN6L2EFerJaYJEuQdWj7VSV1ZE/edit?usp=sharing", "name": "The Bullring"}, 
  {"date": "12-03-23", "recap": "https://docs.google.com/document/d/1FHg9DcKpOsEIQHPLYPphYZnokD0y4n7gJ9apNx9zL68/edit?usp=drive_link", "name": "Las Vegas Motor Speedway Outfield Road Course"}, 
  {"date": "12-31-23", "recap": "https://docs.google.com/document/d/1ba4jXLDbRUTiobNTPBXi0Eolfthc5UP4pmyLNedLM5Y/edit?usp=sharing", "name": "Caldwell Indoor Speedway"}, 
  {"date": "2-08-24", "recap": "https://docs.google.com/document/d/19zszvcrguf1fHgJ5a58e_HNi2GfPKLoBf2izrQiFSzU/edit?usp=sharing", "name": "All-Tech Raceway"}, 
  {"date": "3-01-24", "recap": "https://docs.google.com/document/d/1FowO3JEipMt57b0358Lrx9kXqX-ln3QYjIBq1MdORu0/edit?usp=sharing", "name": "Nitrodome at Planet Hollywood"}, 
  {"date": "4-06-24", "recap": "https://docs.google.com/document/d/1gUdTYDESHiv2u-07d9T8jeL9mwldL8dmhMwz9CjGwCs/edit?usp=sharing", "name": "Eagle Canyon Raceway"}, 
  {"date": "5-17-24", "recap": "https://docs.google.com/document/d/126T19PClImreuAm6iHQNPrk1MgJkSO_-beScmXuL8y4/edit?usp=sharing", "name": "Lakeside Speedway"}, 
  {"date": "5-19-24", "recap": "https://docs.google.com/document/d/1YPLQy23vvKgSj6EU0d2Un74ktLJWD-5BYi59H0KI7DY/edit?usp=sharing", "name": "Sweet Springs Motorsports Complex"}, 
  {"date": "7-25-24", "recap": "https://docs.google.com/document/d/1z8W2gh3euPK1a4k_o8KNjiEn2MtqzvpjgxIKZpldM3k/edit?usp=sharing", "name": "Ripley County Fairgrounds"}, 
  {"date": "7-25-24", "recap": "https://docs.google.com/document/d/1HjDcRuARQvicjdSb3jLLL8bnB-Fv6Gcj8i3qZGqd-40/edit?usp=sharing", "name": "Brownstown Speedway"}, 
  {"date": "8-01-24", "recap": "https://docs.google.com/document/d/1u1jT32JA5dmYG9M4Zh0Wkgp5Xj0rN2FSgykEn_FLOuw/edit?usp=sharing", "name": "Terre Haute Action Track"}, 
  {"date": "8-10-24", "recap": "https://docs.google.com/document/d/1xtkRLDVJgL5pFHADHCjuCSOHdNZXL7zYMNT6ZEqJOrI/edit?usp=sharing", "name": "Bolton Fairgrounds"}, 
  {"date": "8-25-24", "recap": "https://docs.google.com/document/d/195Fl-erNSOVpBk_PgS_VhKIo-TSSVsjT-ThQ2MriEnA/edit?usp=sharing", "name": "MX101"}, 
  {"date": "8-31-24", "recap": "https://docs.google.com/document/d/1O6KuSNrBqG_wzLkYBeke7WgGBTn4_hp2LoV-HaoAhSk/edit?usp=sharing", "name": "The Milwaukee Mile"}, 
  {"date": "8-31-24", "recap": "https://docs.google.com/document/d/1NSios-9_nNPmNVPQwtSa5efJR2WoH18dpNewaFjkNx8/edit?usp=sharing", "name": "Jefferson Speedway"}, 
  {"date": "9-01-24", "recap": "https://docs.google.com/document/d/1T93mxhCWrFbD5vgYtU4yj9THLyy6ruJJdyQPxAHPe98/edit?usp=sharing", "name": "Angell Park Speedway"}, 
  {"date": "9-08-24", "recap": "https://docs.google.com/document/d/1xcLTUB98ZpBY53PAES-Nu4IuU1lq6XPrqUrqhuykwUg/edit?usp=sharing", "name": "508 International"}, 
  {"date": "9-14-24", "recap": "https://docs.google.com/document/d/1aSB70hZwo__qkZG2AZQCydp9RoEeqKJvSJS6ip2m6-c/edit?usp=sharing", "name": "Sportsdrome Speedway"}, 
  {"date": "11-16-24", "recap": "https://docs.google.com/document/d/1vQqZS5ClIZKhrPxOMv_zqQmrriGI8ISydW4gftnUw4U/edit?usp=drive_link", "name": "Buttonwillow Raceway Park"}, 
  {"date": "11-16-24", "recap": "https://docs.google.com/document/d/1bWEHm2ZljZ316-j-NqjfHKeGgwgKbzk5oKXxGjYlVsc/edit?usp=drive_link", "name": "Kevin Harvick's Kern Raceway (Inner Asphalt Oval)"}, 
  {"date": "11-20-24", "recap": "https://docs.google.com/document/d/1Kd3u5djapJMpt2fZ85sXF-Cy_Sl6206c168o75GeKKA/edit?usp=drive_link", "name": "Tulare Thunderbowl Raceway"}, 
  {"date": "11-22-24", "recap": "https://docs.google.com/document/d/1TyKgzGYdK8xxp79RrU_AGYW-Mai0Qwcl7TEZ76niuWE/edit?usp=drive_link", "name": "Las Vegas Strip Circuit"}, 
  {"date": "3-01-25", "recap": "https://docs.google.com/document/d/1J0gtdirMqH9fcHP5xkd4ZuP0EuGVGPXPhH7Izt-TcSA/edit?usp=sharing", "name": "Northwood Lake"}, 
  {"date": "3-22-25", "recap": "https://docs.google.com/document/d/1gmBgxQmQDcjzGTiLTqJLLDf1Ll121xwSFEAbx6-z0M4/edit?usp=sharing", "name": "Boss Ice Arena"}, 
  {"date": "4-18-25", "recap": "https://docs.google.com/document/d/1VN4FkUmFSQJBjiOcjACULZQOGJeu9gsLkiPC6Ogz1JY/edit?usp=drive_link", "name": "Wake County Speedway"}, 
  {"date": "4-19-25", "recap": "https://docs.google.com/document/d/1ugSALJN3lRRIa1ROZpWqXtk3PBh14uOVLqGRCiQwfrw/edit?usp=drive_link", "name": "Rockfish Speedway"}, 
  {"date": "5-09-25", "recap": "https://docs.google.com/document/d/1Lq0cVMMbxkmaCyPntey8bbisVSKVO7GCZvvyiYJhrjU/edit?usp=drive_link", "name": "US 36 Raceway"}, 
  {"date": "5-10-25", "recap": "https://docs.google.com/document/d/1uDF5Y5LYHzx3ajLk0IWDYu8X-lxUqgwmbXpyisCvtJE/edit?usp=drive_link", "name": "I-35 Speedway"}, 
  {"date": "5-11-25", "recap": "https://docs.google.com/document/d/1bqTCLMLMaJfZeQGUUBT0f98JqNcgZ7keVSYtLhlgJNU/edit?usp=drive_link", "name": "Double X Speedway"}, 
  {"date": "5-24-25", "recap": "https://docs.google.com/document/d/1qXba2SIzzNzfO5ktpo2wlCqyfGby0KhDbRLSDxeZcjY/edit?usp=drive_link", "name": "Anderson Speedway"}, 
  {"date": "5-26-25", "recap": "https://docs.google.com/document/d/1yICnY6sPV99EEkTa6XVlwC8bc8xgFM64QbEJ3qHlRe4/edit?usp=sharing", "name": "Atomic Speedway"}, 
  {"date": "6-28-25", "recap": "https://docs.google.com/document/d/1zvnP-r7mcl-hbU_Gik7V-MejmsSeHpdalVO4QJ_EX8U/edit?usp=drive_link", "name": "Oswego Speedway"}, 
  {"date": "6-29-25", "recap": "https://docs.google.com/document/d/1lckD_YOC614Mg_ox7WqhSmP2J2nHvpNX2EVBMakDXi0/edit?usp=drive_link", "name": "Millstream Speedway"}, 
  {"date": "7-11-25", "recap": "https://docs.google.com/document/d/1UN0_yb-HXSpDZXEfi82VPwdQHer1aWVofKuiX9hQo-U/edit?usp=drive_link", "name": "Gallatin Speedway"}, 
  {"date": "7-12-25", "recap": "https://docs.google.com/document/d/1sFMHo-Gx11-kRSFkw76sgEdmuh0oP2zZmja7fT0nItk/edit?usp=drive_link", "name": "Electric City Speedway"}, 
  {"date": "7-22-25", "recap": "https://docs.google.com/document/d/1-vVuvSCt2ljQrXPVEw1kmAWXb4NQJTgn_LSehPeYCU0/edit?usp=drive_link", "name": "Rapid Speedway"}, 
  {"date": "7-23-25", "recap": "https://docs.google.com/document/d/1nAR8Gz3qlEO3N_6XW1mX4AmlcnPTlSJTHg6Pj4AjFIg/edit?usp=sharing", "name": "Maquoketa Speedway"}, 
  {"date": "7-23-25", "recap": "https://docs.google.com/document/d/1ar4keUn6cMVr4jaciVJpoFkD6_uMKyO3-ioFevqtlSw/edit?usp=sharing", "name": "Dubuque Speedway"}, 
  {"date": "7-24-25", "recap": "https://docs.google.com/document/d/1QRii-Aw0pV0zVyQ3W9GM-KP_SB6s9vZrCRWwtWyTR2Y/edit?usp=sharing", "name": "The Dirt Track and Indianapolis Motor Speedway"}, 
  {"date": "7-26-25", "recap": "https://docs.google.com/document/d/1Np7_yEx0SZqQJL_ECz-rq2qZTsrLKKD5OD4bKH8FNy8/edit?usp=drive_link", "name": "US 24 Speedway"}, 
  {"date": "8-05-25", "recap": "https://docs.google.com/document/d/1Fwd2d3m8p00_GPA0W0Yx3MdqVWIFmKTRub7bcD2y7fk/edit?usp=sharing", "name": "Mohawk International Speedway"}, 
  {"date": "8-24-25", "recap": "https://docs.google.com/document/d/1u8br1W3ga6XZeqyPZxkBh9HDwNuA0DDu6rcE0Cv31QY/edit?usp=drive_link", "name": "Capeway Rovers"}, 
  {"date": "9-11-25", "recap": "https://docs.google.com/document/d/16FEggqnBC4snRvawij9AS05dH8xYDs-YTa7x-KQKijY/edit?tab=t.0", "name": "Berlin Fair"}, 
  {"date": "9-27-25", "recap": "https://docs.google.com/document/d/1uwuWm7WHW9pPs68CCc4gj8_0z5WJsIccW-_iEa_WUZc/edit?usp=sharing", "name": "Hawkeye Downs Speedway (Dirt)"}, 
  {"date": "9-28-25", "recap": "https://docs.google.com/document/d/1u3wR1zS10CfGjy3NBsxA4kt1j1wjGt4vnvQRCu3QVy0/edit?usp=drive_link", "name": "Cole's County Speedway"}, 
  {"date": "11-25-25", "recap": "https://docs.google.com/document/d/1nG5cPx5aVP0IJOIZme9HeXlpB5Q9Z0uCsBgEaf_6APc/edit?usp=sharing", "name": "Bakersfield Speedway at Kevin Harvick's Kern Raceway"}, 
  {"date": "11-08-25", "recap": "https://docs.google.com/document/d/1b2fpOQqjKEwCdD_iVEKpZqykA1BhzJAdkGQS27LMz3U/edit?usp=sharing", "name": "Glen Helen Raceway (Dirt)"}
]
"""


input = """
<a href="https://docs.google.com/document/d/1NY7k5ZdvMczqQ2cToR47BTQnS27GM3610PHW8iY0lZQ/edit?usp=sharing" target="_blank">2-01-20: Boardwalk Hall</a>
      <br/>
      <a href="https://docs.google.com/document/d/1gJqvKgNog4KVhEHmJIVhhf8GCnKOm2ZCXYQ2H7nIzM4/edit?usp=sharing" target="_blank">6-16-20: Paragon Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1NlYWfZVLht_UwNYtHa-7p65voO4GlXjnLxh_KkK_o0Y/edit?usp=sharing" target="_blank">6-19-20: Tri-State Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/14xdSQpGZenzPFbWwTEVv66lM-tgusrEKlxeOzbX8KAc/edit?usp=sharing" target="_blank">7-03-20: Big Diamond Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1EtTQTugt0_Mw0hXvZv4SdsHsy1e1tujFf634Inm-Gbk/edit?usp=sharing" target="_blank">7-04-20: White Mountain Motorsports Park</a>
      <br/>
      <a href="https://docs.google.com/document/d/1KKiLqBxGqsEDS_sP7dcQN1SXmfaA8WSqDSZUwHnrrKU/edit?usp=sharing" target="_blank">8-01-20: Londonderry Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Wuo6WNWFi39lUxDThPQvvv7ClVCO-ZO4-R_6kaOrqtQ/edit?usp=sharing" target="_blank">8-21-20: Lucas Oil Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1JOzXzV5dWs1pkkGUJ49p91UnN6FlQxi4uoikMSOGMJ8/edit?usp=sharing" target="_blank">8-23-20: Indiana State Fairgrounds</a>
      <br/>
      <a href="https://docs.google.com/document/d/10wz-9ODQhCdf-G2QdlYHLyQeKkfXIv21mjsZLRs3I5E/edit?usp=sharing" target="_blank">9-12-20: New Hampshire Motor Speedway Legends Oval</a>
      <br/>
      <a href="https://docs.google.com/document/d/1kJyQOA3ces6SEA0JNmJFrRRRFzPVcvQXpkavjmmTXwo/edit?usp=sharing" target="_blank">1-31-21: Lee Pond</a>
      <br/>
      <a href="https://docs.google.com/document/d/1uVg5Ohk6ZKgTdaSJPtomYtPOFiLyU-G4YZvrrf6t4ns/edit?usp=sharing" target="_blank">3-06-21: Rochester Fairgrounds</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Cmbm8ZPXGMjbTYtg4OoMB3Vfv3in7nth9t_QcwScQXM/edit?usp=sharing" target="_blank">3-26-21: Boyd's Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1T9WVdlRPcuie9G1TApOcL0QG7V-lp214QGvxcjISZIA/edit?usp=sharing" target="_blank">5-08-21: Rochester Fairgrounds (Road Course)</a>
      <br/>
      <a href="https://docs.google.com/document/d/1HUCtDeaBU6EZqZF5RCsLEatfio0AZBndus-wy8dHusA/edit?usp=sharing" target="_blank">5-23-21: Central Cycle Club</a>
      <br/>
      <a href="https://docs.google.com/document/d/1_x7UtZxyb2uPf17I-WoQkrFZh73FCOoYA7Gz7Lx0GsE/edit?usp=sharing" target="_blank">5-23-21: Pomfret Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1cF1Y-QeVOz6HNsb2F7ymF72NLLy-HOlkNfqwg1GJojo/edit?usp=sharing" target="_blank">5-29-21: Fulton Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1-Bf2hFWNjW1brrH5yBAPVWeKA0QTLsx2fOsQgyb3vm0/edit?usp=sharing" target="_blank">6-13-21: Action Track USA</a>
      <br/>
      <a href="https://docs.google.com/document/d/1jMUlM44lKosb2e5Hw0G9kQUYg1-auFUfvk_7tvORAOA/edit?usp=sharing" target="_blank">6-14-21: Wayne County Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1-vJNUO0HReic3QRckm27whW_tLF75LkzIZedVp7q_RA/edit?usp=sharing" target="_blank">6-19-21: Path Valley Speedway Park</a>
      <br/>
      <a href="https://docs.google.com/document/d/1dlKKKhfcHdsTPexN3efjKSq_kEe_Zu3YKMd8wfZgLGE/edit?usp=sharing" target="_blank">6-20-21: Selinsgrove Raceway Park</a>
      <br/>
      <a href="https://docs.google.com/document/d/1qY46UKPuyo0DyH03f1_4N_Ka2MP-zQjDmM0QrTOCIGA/edit?usp=sharing" target="_blank">6-20-21: Bloomsburg Fair Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1fZmpM_dK53k1XD1uFWTdK87kTXnH60bJWJQ1KpXhJn0/edit?usp=sharing" target="_blank">6-26-21: Riverhead Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1CY-ep1JF6d2orvtvh8oz6gaQorIfsBWFIptMfS8jFy0/edit?usp=sharing" target="_blank">7-08-21: KRA Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Bw1HcyUPJwhMolZsvYC8JkvQE9ry6WTudaRjuPkL5og/edit?usp=sharing" target="_blank">7-10-21: ERX Motor Park</a>
      <br/>
      <a href="https://docs.google.com/document/d/1btVwp8LM-6Q4S8tPVAzdLTsVzynMoD8EcI2G_ENPIzk/edit?usp=sharing" target="_blank">8-21-21: Perris Auto Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1u_Mx9-J5ApGQ3x6562fa1teoJuRYLDARj7_DuB2C1QQ/edit?usp=sharing" target="_blank">9-10-21: Huset's Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1k68ABZnlcbOm8ZzaRrAXJVTcJh4_UO08KvfKjYKqXnA/edit?usp=sharing" target="_blank">10-02-21: Talladega Superspeedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1SxHar13_X1DDIvXW8uDMHoM6nDsolFXN0PLk-rxPBnM/edit?usp=sharing" target="_blank">10-02-21: Talladega Short Track</a>
      <br/>
      <a href="https://docs.google.com/document/d/15KjPfsdFj6AHZXhDFu9egy4Gt481T7A5chQIAk83zm0/edit?usp=sharing" target="_blank">10-11-21: Topsfield Fair</a>
      <br/>
      <a href="https://docs.google.com/document/d/1YszGHme3-q9X9SgUYqWXc-VyEhS8B9BHQHODCDXCOpI/edit?usp=sharing" target="_blank">11-12-21: Arizona Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Z5YTOHT81HoclolnJAomHC3hgmE-L-iP5sPPlyTBRCY/edit?usp=sharing" target="_blank">11-20-21: Perris Auto Speedway (Figure-8, Inner Oval, Road Course)</a>
      <br/>
      <a href="https://docs.google.com/document/d/1vSoctG7H6KN6MjDYqTSBwHF6pm314P0HVKKk7qUYgIc/edit?usp=sharing" target="_blank">1-27-22: Cocopah Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1BCBJbbBOcCUcQgaYMhX10NafgDVv1zVkEZmHhV2zGog/edit?usp=sharing" target="_blank">2-05-22: Irwindale Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/17I03RuIsZzwAsp66-2LxH3i5DBYn1H2xigY53PsEtgU/edit?usp=sharing" target="_blank">2-06-22: Los Angeles Memorial Colisum</a>
      <br/>
      <a href="https://docs.google.com/document/d/1_iSHK60CfFMC6qBIbdU9P5RqFcJO79D3imj_70SrnI0/edit?usp=sharing" target="_blank">3-18-22: Hickory Motor Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1_fSjP3YH0T0ZWSLWAwYl-_WzgHDXrOeDf5coCBdODT4/edit?usp=sharing" target="_blank">3-18-22: Carolina Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Dc-XE-gm02P41M8cX6vA24AnJEZW0n-W85eq0u2WIHs/edit?usp=sharing" target="_blank">3-26-22: Cherokee Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1AhQjZiDoXSCiT0CZoTgtPYhdnFKdi3lKZR9ijobAsmo/edit?usp=sharing" target="_blank">6-11-22: Ventura Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1fdsuRQeIrU5tNUQtGvzzaimkmG68T7fQcQI05-peTks/edit?usp=sharing" target="_blank">6-18-22: Bakersfield Speedway (Inner)</a>
      <br/>
      <a href="https://docs.google.com/document/d/1TArP-p33CCSbzo5fjXRD0T1sd_O_NqK-HEMaGUBSv1A/edit?usp=sharing" target="_blank">6-18-22: Kern County Raceway (Asphalt))</a>
      <br/>
      <a href="https://docs.google.com/document/d/1OOLMCagoDsybCN9Lwl4WEODLKFUWR9VDToevCP7Z0KQ/edit?usp=sharing" target="_blank">6-23-22: Skagit Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1M2-FOnTfNowCwr3cCR_S-gr09tc4T5tu27oJBRSG3c4/edit?usp=sharing" target="_blank">7-18-22: Greenwood Valley Action Tracks</a>
      <br/>
      <a href="https://docs.google.com/document/d/1n_uz8ccI1RqW51nEa1yFo05IqQ-LKf4r3Sual1ARnGo/edit?usp=sharing" target="_blank">7-21-22: Linda's Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Bg6ST4Wqj-r7WkhBVXdIokKVgRcMAwfej6nX9S2EzwY/edit?usp=sharing" target="_blank">7-25-22: Circle City Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Q4Kmi7RdIEinGkxn1jvn6Jomy1lUfOyyzJ2hRytx8jM/edit?usp=sharing" target="_blank">7-27-22: Pendleton County Fairgrounds</a>
      <br/>
      <a href="https://docs.google.com/document/d/19qrE3wIL4vhjl24sH96GAa_CfKitODL1s-zrG_wJRwg/edit?usp=sharing" target="_blank">7-29-22: Bloomington Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1R1PeRd2QQ5ANKIBhwL4OedMQxyHqZdvNpeaBZjnyQCE/edit?usp=sharing" target="_blank">7-31-22: Dirt City Motorplex</a>
      <br/>
      <a href="https://docs.google.com/document/d/1O0yxPre_MK0auw3uxa2OIjKdp69heqw1tejIMViVDtQ/edit?usp=sharing" target="_blank">8-14-22: New Hampshire Motor Speedway Road Course (Full)</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Dkty51LP-qxLMXsT2U_FhX2T8cRTEwp7954tpHIxHI8/edit?usp=sharing" target="_blank">8-19-22: Outlaw Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Gp0Igi_6eBAcVrAK14o3o1gXzBgVfcpGZaYB6ZVv1e4/edit?usp=sharing" target="_blank">8-20-22: Skyline Raceway Motorsports Park</a>
      <br/>
      <a href="https://docs.google.com/document/d/1fVZBEgPEHSrMXNTERhDK1Oot035Ub4Bh12jOYCu-d3Y/edit?usp=sharing" target="_blank">8-20-22: Five Mile Point Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1m6lw-P_mLKPR1nfu1CUmHMpi_v0etaT7i4W1FB-QmuA/edit?usp=sharing" target="_blank">9-30-22: I-30 Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1xgMoNdnybQSwvDL_0o7EeMXmyXNk3jOkvV5gnrdBgmc/edit?usp=sharing" target="_blank">10-06-22: Tri-County Racetrack</a>
      <br/>
      <a href="https://docs.google.com/document/d/1a1ejb20ge3ksqiHRKJCawQjEbOA1wAJDiS_HnF79F30/edit?usp=sharing" target="_blank">10-08-22: Nashville Fairgrounds Speedway (Inner)</a>
      <br/>
      <a href="https://docs.google.com/document/d/11Ofpyvo46MBpJd3JB4mHhmSAFn2gyAkQ5zTYofvLyxM/edit?usp=sharing" target="_blank">10-11-22: 411 Motor Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1NmgNoN75-Tjb9U5RTKs1Au20t5tE-SLKBPNuO6YroD0/edit?usp=sharing" target="_blank">11-12-22: Adobe Mountain Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/11SfqzFBMiZeI6gk4UmyAKP8e-uqcrnQQn-JY5ueK-zU/edit?usp=sharing" target="_blank">11-15-22: Bakersfield Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1rIIH_l2GhHZKOUQ9azU08F6W3yobhEx9rymBFkw3Qo4/edit?usp=sharing" target="_blank">12-17-22: Southern Illinois Center</a>
      <br/>
      <a href="https://docs.google.com/document/d/14QvuES0oEQNPas13F_ZV_cfFX4ILCbfK-EQO7zk7R_4/edit?usp=sharing" target="_blank">1-21-23: Circuit de Trois Rivieres Rallycross</a>
      <br/>
      <a href="https://docs.google.com/document/d/1_i7Xw_zy7f7xMOrwF7dGHwNEux-OeH8Fm3JuIOReGFQ/edit?usp=sharing" target="_blank">2-09-23: Volusia Speedway Park</a>
      <br/>
      <a href="https://docs.google.com/document/d/11Pg9Z2GVXR79qUS-Jgw_jtbg15mQjyd1rUswv4VlbUE/edit?usp=sharing" target="_blank">2-10-23: Auburndale Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1ro6-p7BEPoCU8hcNU8xZKW8pMEXMcoPhJ4u16U5-FkM/edit?usp=sharing" target="_blank">2-10-23: Showtime Speedway (Oval and Figure-8)</a>
      <br/>
      <a href="https://docs.google.com/document/d/1UWfVlUCVHohfQSZLCLWHJRYP3efzYdsMATXerDVUeps/edit?usp=sharing" target="_blank">2-11-23: Hobe Sound Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1mvRNAsOzxlIovYom9Or6aaYuKKye5pneYkwksTQA4xw/edit?usp=sharing" target="_blank">2-11-23: Hendry County Motorsports Park</a>
      <br/>
      <a href="https://docs.google.com/document/d/1w8WcgOkN906qGp78tAyxHIjRhOw6TCx21Xc3TtJA6Yo/edit?usp=sharing" target="_blank">2-12-23: New Smyrna Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1IkljAMfplrLVPvEldvDBVEGDjYRgCbS8Uinqc8LHyjM/edit?usp=sharing" target="_blank">2-13-23: East Bay Raceway Park</a>
      <br/>
      <a href="https://docs.google.com/document/d/1YJpOtM7ofRdTjp9jpDUiGzxT8rAzcs3lEqGjKdkDZsI/edit?usp=sharing" target="_blank">2-16-23: Citrus County Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1a5FV--NhwjTZ_mAuqKYkQigWjme6qbsyx88P727_Yjw/edit?usp=sharing" target="_blank">2-16-23: Bubba Raceway Park</a>
      <br/>
      <a href="https://docs.google.com/document/d/13gPGQCSHwjn-2hagP2YMB0V3OEwPItnYlj1e0XO7yBs/edit?usp=sharing" target="_blank">5-19-23: Clinton County Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1P5K6V0GQtRodNLoMcysHIMsp65WHYvH9G8cmuhTAUTA/edit?usp=sharing" target="_blank">5-20-23: Bowman Gray Stadium</a>
      <br/>
      <a href="https://docs.google.com/document/d/1MRi774EQu4-RPp9-cxXbfeac35L2PR85CfQ8AIfgxGY/edit?usp=sharing" target="_blank">5-28-23: Wiscasset Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1xRaCTrM6tAow4wu7A8P86p4dbxwptctXe3uQsVS4sFs/edit?usp=sharing" target="_blank">7-02-23: Chicago Street Course</a>
      <br/>
      <a href="https://docs.google.com/document/d/1FXwlH6jL0VPuczJj_0IkkHdZnRen8j9fgXg5ck8VPAU/edit?usp=sharing" target="_blank">7-03-23: Rockford Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/17oZDDJ7k__B2dWp35OGNjrQp-1AbMpg6n4xZav2WCgQ/edit?usp=sharing" target="_blank">7-04-23: What Cheer Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1gAqlMxUiyNDHWiktJZDbmtV5DB8nOVgEqG-R7Zbqf94/edit?usp=sharing" target="_blank">7-05-23: Independence Motor Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1WFw_Q2LbU7oZRxO8ssiYaj0DFGiS-xPheVrhpwlTGtg/edit?usp=sharing" target="_blank">7-07-23: Farmer City Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1T6lqbapYMhBwThFdZTxuiV0bz3mYv58mLlij2WZMK68/edit?usp=sharing" target="_blank">7-15-23: NHMX Flat Track</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Ayg89A_o3pJUCjYky7f8ThbUMnmLevr8wVP6Ipp1NE0/edit?usp=sharing" target="_blank">7-23-23: Pocono Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1kk1dKll-L6jv1WGo9N3t4tnk0-DRSEHL674_ZmX_o5c/edit?usp=sharing" target="_blank">8-12-23: Winchester Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Je4ZTS-7hgr2dPM123eBsJ3S2kt7KvQfsTsFFqknkxQ/edit?usp=sharing" target="_blank">8-26-23: Marshfield Fair</a>
      <br/>
      <a href="https://docs.google.com/document/d/1dHYUgXgJasMN9YRgKtZr5x8RLhXs4dyErkEbRibCjdw/edit?usp=sharing" target="_blank">9-29-23: Unity Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1MlBEpqJr69vPNIy5vSUZiE40QnWz9xeWyPpSCkTwxYU/edit?usp=sharing" target="_blank">9-30-23: Thompson Speedway (Asphalt Road Course)</a>
      <br/>
      <a href="https://docs.google.com/document/d/11pgOum_uPd6dvrBMGz-dA3c2O2FKq9BLFV08oN2fbuI/edit?usp=sharing" target="_blank">10-20-23: Devil's Bowl Speedway (TX)</a>
      <br/>
      <a href="https://docs.google.com/document/d/13NEjgH_MhmIjhm5JAzo-lnBKtliHMG5Gvd4F4CNmX1Q/edit?usp=sharing" target="_blank">11-04-23: Stockton Dirt Track</a>
      <br/>
      <a href="https://docs.google.com/document/d/1TmZPUVQiXJA85dInqKaIPd_mjZDgwwlOKSqblb75NlA/edit?usp=sharing" target="_blank">11-05-23: SBC Fairgrounds</a>
      <br/>
      <a href="https://docs.google.com/document/d/1D1uQOG7PMklUKOL1BOUZl9GPjVte7N1DRCAbVQQ9UWo/edit?usp=sharing" target="_blank">11-10-23: Central Arizona Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1re-5NPavMWakhjQsAAXrgWLP4LW_BvTrdzNKCrhzaN4/edit?usp=sharing" target="_blank">11-11-23: Podium Club at Attesa (Full Course)</a>
      <br/>
      <a href="https://docs.google.com/document/d/1kZgS1EOsRGdaSLQsawPjQ1j1Grr3kr9P6B-H0B3QlWE/edit?usp=sharing" target="_blank">11-12-23: Shorty's Sports Park</a>
      <br/>
      <a href="https://docs.google.com/document/d/1-74uKcHC0Px-KrsNWaVaAkV2LkO4s_-Ve-sp6vNnEoA/edit?usp=sharing" target="_blank">11-17-23: Placerville Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1aX8mYQEKPC9OhaaoGxTfESQN67wknyB2yakUWw_fv7A/edit?usp=sharing" target="_blank">11-21-23: Merced Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1eHpzJxAEA7KSw74zOtN6L2EFerJaYJEuQdWj7VSV1ZE/edit?usp=sharing" target="_blank">12-01-23: The Bullring</a>
      <br/>
      <a href="https://docs.google.com/document/d/1FHg9DcKpOsEIQHPLYPphYZnokD0y4n7gJ9apNx9zL68/edit?usp=drive_link" target="_blank">12-03-23: Las Vegas Motor Speedway Outfield Road Course</a>
      <br/>
      <a href="https://docs.google.com/document/d/1ba4jXLDbRUTiobNTPBXi0Eolfthc5UP4pmyLNedLM5Y/edit?usp=sharing" target="_blank">12-31-23: Caldwell Indoor Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/19zszvcrguf1fHgJ5a58e_HNi2GfPKLoBf2izrQiFSzU/edit?usp=sharing" target="_blank">2-08-24: All-Tech Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1FowO3JEipMt57b0358Lrx9kXqX-ln3QYjIBq1MdORu0/edit?usp=sharing" target="_blank">3-01-24: Nitrodome at Planet Hollywood</a>
      <br/>
      <a href="https://docs.google.com/document/d/1gUdTYDESHiv2u-07d9T8jeL9mwldL8dmhMwz9CjGwCs/edit?usp=sharing" target="_blank">4-06-24: Eagle Canyon Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/126T19PClImreuAm6iHQNPrk1MgJkSO_-beScmXuL8y4/edit?usp=sharing" target="_blank">5-17-24: Lakeside Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1YPLQy23vvKgSj6EU0d2Un74ktLJWD-5BYi59H0KI7DY/edit?usp=sharing" target="_blank">5-19-24: Sweet Springs Motorsports Complex</a>
      <br/>
      <a href="https://docs.google.com/document/d/1z8W2gh3euPK1a4k_o8KNjiEn2MtqzvpjgxIKZpldM3k/edit?usp=sharing" target="_blank">7-25-24: Ripley County Fairgrounds</a>
      <br/>
      <a href="https://docs.google.com/document/d/1HjDcRuARQvicjdSb3jLLL8bnB-Fv6Gcj8i3qZGqd-40/edit?usp=sharing" target="_blank">7-25-24: Brownstown Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1u1jT32JA5dmYG9M4Zh0Wkgp5Xj0rN2FSgykEn_FLOuw/edit?usp=sharing" target="_blank">8-01-24: Terre Haute Action Track</a>
      <br/>
      <a href="https://docs.google.com/document/d/1xtkRLDVJgL5pFHADHCjuCSOHdNZXL7zYMNT6ZEqJOrI/edit?usp=sharing" target="_blank">8-10-24: Bolton Fairgrounds</a>
      <br/>
      <a href="https://docs.google.com/document/d/195Fl-erNSOVpBk_PgS_VhKIo-TSSVsjT-ThQ2MriEnA/edit?usp=sharing" target="_blank">8-25-24: MX101</a>
      <br/>
      <a href="https://docs.google.com/document/d/1O6KuSNrBqG_wzLkYBeke7WgGBTn4_hp2LoV-HaoAhSk/edit?usp=sharing" target="_blank">8-31-24: The Milwaukee Mile</a>
      <br/>
      <a href="https://docs.google.com/document/d/1NSios-9_nNPmNVPQwtSa5efJR2WoH18dpNewaFjkNx8/edit?usp=sharing" target="_blank">8-31-24: Jefferson Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1T93mxhCWrFbD5vgYtU4yj9THLyy6ruJJdyQPxAHPe98/edit?usp=sharing" target="_blank">9-01-24: Angell Park Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1xcLTUB98ZpBY53PAES-Nu4IuU1lq6XPrqUrqhuykwUg/edit?usp=sharing" target="_blank">9-08-24: 508 International</a>
      <br/>
      <a href="https://docs.google.com/document/d/1aSB70hZwo__qkZG2AZQCydp9RoEeqKJvSJS6ip2m6-c/edit?usp=sharing" target="_blank">9-14-24: Sportsdrome Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1vQqZS5ClIZKhrPxOMv_zqQmrriGI8ISydW4gftnUw4U/edit?usp=drive_link" target="_blank">11-16-24: Buttonwillow Raceway Park</a>
      <br/>
      <a href="https://docs.google.com/document/d/1bWEHm2ZljZ316-j-NqjfHKeGgwgKbzk5oKXxGjYlVsc/edit?usp=drive_link" target="_blank">11-16-24: Kevin Harvick's Kern Raceway (Inner Asphalt Oval)</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Kd3u5djapJMpt2fZ85sXF-Cy_Sl6206c168o75GeKKA/edit?usp=drive_link" target="_blank">11-20-24: Tulare Thunderbowl Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1TyKgzGYdK8xxp79RrU_AGYW-Mai0Qwcl7TEZ76niuWE/edit?usp=drive_link" target="_blank">11-22-24: Las Vegas Strip Circuit</a>
      <br/>
      <a href="https://docs.google.com/document/d/1J0gtdirMqH9fcHP5xkd4ZuP0EuGVGPXPhH7Izt-TcSA/edit?usp=sharing" target="_blank">3-01-25: Northwood Lake</a>
      <br/>
      <a href="https://docs.google.com/document/d/1gmBgxQmQDcjzGTiLTqJLLDf1Ll121xwSFEAbx6-z0M4/edit?usp=sharing" target="_blank">3-22-25: Boss Ice Arena</a>
      <br/>
      <a href="https://docs.google.com/document/d/1vEcKBZQkwi9mISd0To0h819qd8VyE9lDZk2wc_uVHng/edit?usp=drive_link" target="_blank">4-18-25 and 4-19-25: Rockingham Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1VN4FkUmFSQJBjiOcjACULZQOGJeu9gsLkiPC6Ogz1JY/edit?usp=drive_link" target="_blank">4-18-25: Wake County Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1ugSALJN3lRRIa1ROZpWqXtk3PBh14uOVLqGRCiQwfrw/edit?usp=drive_link" target="_blank">4-19-25: Rockfish Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Lq0cVMMbxkmaCyPntey8bbisVSKVO7GCZvvyiYJhrjU/edit?usp=drive_link" target="_blank">5-09-25: US 36 Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1uDF5Y5LYHzx3ajLk0IWDYu8X-lxUqgwmbXpyisCvtJE/edit?usp=drive_link" target="_blank">5-10-25: I-35 Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1bqTCLMLMaJfZeQGUUBT0f98JqNcgZ7keVSYtLhlgJNU/edit?usp=drive_link" target="_blank">5-11-25: Double X Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1qXba2SIzzNzfO5ktpo2wlCqyfGby0KhDbRLSDxeZcjY/edit?usp=drive_link" target="_blank">5-24-25: Anderson Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1yICnY6sPV99EEkTa6XVlwC8bc8xgFM64QbEJ3qHlRe4/edit?usp=sharing" target="_blank">5-26-25: Atomic Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1zvnP-r7mcl-hbU_Gik7V-MejmsSeHpdalVO4QJ_EX8U/edit?usp=drive_link" target="_blank">6-28-25: Oswego Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1lckD_YOC614Mg_ox7WqhSmP2J2nHvpNX2EVBMakDXi0/edit?usp=drive_link" target="_blank">6-29-25: Millstream Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1UN0_yb-HXSpDZXEfi82VPwdQHer1aWVofKuiX9hQo-U/edit?usp=drive_link" target="_blank">7-11-25: Gallatin Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1sFMHo-Gx11-kRSFkw76sgEdmuh0oP2zZmja7fT0nItk/edit?usp=drive_link" target="_blank">7-12-25: Electric City Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1-vVuvSCt2ljQrXPVEw1kmAWXb4NQJTgn_LSehPeYCU0/edit?usp=drive_link" target="_blank">7-22-25: Rapid Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1nAR8Gz3qlEO3N_6XW1mX4AmlcnPTlSJTHg6Pj4AjFIg/edit?usp=sharing" target="_blank">7-23-25: Maquoketa Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1ar4keUn6cMVr4jaciVJpoFkD6_uMKyO3-ioFevqtlSw/edit?usp=sharing" target="_blank">7-23-25: Dubuque Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1QRii-Aw0pV0zVyQ3W9GM-KP_SB6s9vZrCRWwtWyTR2Y/edit?usp=sharing" target="_blank">7-24-25: The Dirt Track and Indianapolis Motor Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Np7_yEx0SZqQJL_ECz-rq2qZTsrLKKD5OD4bKH8FNy8/edit?usp=drive_link" target="_blank">7-26-25: US 24 Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1Fwd2d3m8p00_GPA0W0Yx3MdqVWIFmKTRub7bcD2y7fk/edit?usp=sharing" target="_blank">8-05-25: Mohawk International Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1u8br1W3ga6XZeqyPZxkBh9HDwNuA0DDu6rcE0Cv31QY/edit?usp=drive_link" target="_blank">8-24-25: Capeway Rovers</a>
      <br/>
      <a href="https://docs.google.com/document/d/16FEggqnBC4snRvawij9AS05dH8xYDs-YTa7x-KQKijY/edit?tab=t.0" target="_blank">9-11-25: Berlin Fair</a>
      <br/>
      <a href="https://docs.google.com/document/d/1uwuWm7WHW9pPs68CCc4gj8_0z5WJsIccW-_iEa_WUZc/edit?usp=sharing" target="_blank">9-27-25: Hawkeye Downs Speedway (Dirt)</a>
      <br/>
      <a href="https://docs.google.com/document/d/1u3wR1zS10CfGjy3NBsxA4kt1j1wjGt4vnvQRCu3QVy0/edit?usp=drive_link" target="_blank">9-28-25: Cole's County Speedway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1nG5cPx5aVP0IJOIZme9HeXlpB5Q9Z0uCsBgEaf_6APc/edit?usp=sharing" target="_blank">11-25-25: Bakersfield Speedway at Kevin Harvick's Kern Raceway</a>
      <br/>
      <a href="https://docs.google.com/document/d/1b2fpOQqjKEwCdD_iVEKpZqykA1BhzJAdkGQS27LMz3U/edit?usp=sharing" target="_blank">11-08-25: Glen Helen Raceway (Dirt)</a>
      <br/>
"""

# print parse_recaps(input)

# print transform_events(input2)



def replace_iso_dates(input_string):
    """
    Replaces ISO-8601 dates (YYYY-MM-DDTHH:MM:SS.sssZ)
    with M-DD-YYYY (no zero-padding on month).
    """

    def repl(match):
        year = match.group(1)
        month = str(int(match.group(2)))  # remove leading zero
        day = match.group(3)
        return "%s-%s-%s" % (month, day, year)

    pattern = r'(\d{4})-(\d{2})-(\d{2})T\d{2}:\d{2}:\d{2}\.\d+Z'
    return re.sub(pattern, repl, input_string)

input3 = """
{
  "1": {
    "Track": "The Dirt Track at Las Vegas Motor Speedway",
    "Date": "2000-03-03T05:00:00.000Z",
    "State": "NV",
    "City": "Las Vegas",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 36.285462,
    "Longitude": -115.011854,
    "Status": "Permanent"
  },
  "2": {
    "Track": "Las Vegas Motor Speedway",
    "Date": "2000-03-04T05:00:00.000Z",
    "State": "NV",
    "City": "Las Vegas",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 1.5,
    "Latitude": 36.272028,
    "Longitude": -115.01029,
    "Status": "Permanent"
  },
  "3": {
    "Track": "Pocatello Speedway",
    "State": "ID",
    "City": "Pocatello",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 42.912684,
    "Longitude": -112.577022,
    "Status": "Permanent"
  },
  "4": {
    "Track": "Magic Valley Speedway",
    "Date": "2002-09-14T04:00:00.000Z",
    "State": "ID",
    "City": "Twin Falls",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.33,
    "Latitude": 42.486547,
    "Longitude": -114.502064,
    "Status": "Permanent"
  },
  "5": {
    "Track": "Miller Motorsports Park",
    "Date": "2009-05-17T04:00:00.000Z",
    "State": "UT",
    "City": "Tooele",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 3,
    "Latitude": 40.580394,
    "Longitude": -112.378375,
    "Status": "Permanent",
    "Total Races": "#ERROR!"
  },
  "6": {
    "Track": "Phoenix International Raceway",
    "Date": 2009,
    "State": "AZ",
    "City": "Avondale",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 1,
    "Latitude": 33.37478,
    "Longitude": -112.310508,
    "Status": "Permanent"
  },
  "7": {
    "Track": "Rocky Mountain Raceways",
    "Date": "2010-09-19T04:00:00.000Z",
    "State": "UT",
    "City": "West Valley City",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.375,
    "Latitude": 40.71917,
    "Longitude": -112.046914,
    "Status": "Permanent"
  },
  "8": {
    "Track": "Rocky Mountain Raceways (Asphalt Figure 8)",
    "Date": "2010-09-19T04:00:00.000Z",
    "State": "UT",
    "City": "West Valley City",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Status": "Permanent"
  },
  "9": {
    "Track": "Atomic Motor Raceway",
    "Date": "2010-09-25T04:00:00.000Z",
    "State": "ID",
    "City": "Atomic City",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 43.446541,
    "Longitude": -112.811413,
    "Status": "Permanent"
  },
  "10": {
    "Track": "Atomic Motor Raceway (Inner Dirt Oval)",
    "State": "ID",
    "City": "Atomic City",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Status": "Permanent"
  },
  "11": {
    "Track": "Stuart Speedway",
    "Date": "2012-07-29T04:00:00.000Z",
    "State": "NE",
    "City": "Stuart",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 42.607193,
    "Longitude": -99.139804,
    "Status": "Permanent"
  },
  "12": {
    "Track": "Wakeeney Speedway",
    "Date": "2012-08-01T04:00:00.000Z",
    "State": "KS",
    "City": "Wakeeney",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 39.024411,
    "Longitude": -99.86834,
    "Status": "Permanent"
  },
  "13": {
    "Track": "Miller Motorsports Park Off Road Course",
    "Date": "2013-06-23T04:00:00.000Z",
    "State": "UT",
    "City": "Tooele",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Latitude": 40.585406,
    "Longitude": -112.385315,
    "Status": "Permanent"
  },
  "14": {
    "Track": "New Hampshire Motor Speedway",
    "Date": "2013-09-22T04:00:00.000Z",
    "State": "NH",
    "City": "Loudon",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 1.058,
    "Latitude": 43.36241,
    "Longitude": -71.460713,
    "Status": "Permanent"
  },
  "15": {
    "Track": "Nassau Coliseum Parking Lot",
    "Date": "2014-07-20T04:00:00.000Z",
    "State": "NY",
    "City": "Uniondale",
    "Type": "Parking Lot",
    "Surface": "Mixed",
    "Latitude": 40.72072,
    "Longitude": -73.589474,
    "Status": "Temporary"
  },
  "16": {
    "Track": "Rocky Mountain Raceways (Inner Asphalt Oval)",
    "Date": "2014-08-16T04:00:00.000Z",
    "State": "UT",
    "City": "West Valley City",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Status": "Permanent"
  },
  "17": {
    "Track": "Rocky Mountain Raceways (Asphalt Road Course)",
    "Date": "2015-08-15T04:00:00.000Z",
    "State": "UT",
    "City": "West Valley City",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Status": "Permanent"
  },
  "18": {
    "Track": "Seekonk Speedway",
    "Date": "2016-07-13T04:00:00.000Z",
    "State": "MA",
    "City": "Seekonk",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.33,
    "Latitude": 41.784545,
    "Longitude": -71.302063,
    "Status": "Permanent"
  },
  "19": {
    "Track": "Pocatello Speedway (Inner Dirt Oval)",
    "Date": "2016-07-23T04:00:00.000Z",
    "State": "ID",
    "City": "Pocatello",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Status": "Permanent"
  },
  "20": {
    "Track": "Seekonk Speedway (Asphalt Figure 8)",
    "Date": "2016-08-07T04:00:00.000Z",
    "State": "MA",
    "City": "Seekonk",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Status": "Permanent"
  },
  "21": {
    "Track": "Thompson Speedway",
    "Date": "2016-08-24T04:00:00.000Z",
    "State": "CT",
    "City": "Thompson",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.625,
    "Latitude": 41.981539,
    "Longitude": -71.824777,
    "Status": "Permanent"
  },
  "22": {
    "Track": "Port of LA",
    "Date": "2016-10-09T04:00:00.000Z",
    "State": "CA",
    "City": "Los Angeles",
    "Type": "Parking Lot",
    "Surface": "Mixed",
    "Latitude": 33.715601,
    "Longitude": -118.274313,
    "Status": "Permanent"
  },
  "23": {
    "Track": "Star Speedway",
    "Date": "2017-04-15T04:00:00.000Z",
    "State": "NH",
    "City": "Epping",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 43.029218,
    "Longitude": -71.040663,
    "Status": "Permanent"
  },
  "24": {
    "Track": "Stafford Motor Speedway",
    "Date": "2017-04-30T04:00:00.000Z",
    "State": "CT",
    "City": "Stafford Springs",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.5,
    "Latitude": 41.955244,
    "Longitude": -72.32045,
    "Status": "Permanent"
  },
  "25": {
    "Track": "Thompson Speedway (Mixed Road Course)",
    "Date": "2017-06-03T04:00:00.000Z",
    "State": "CT",
    "City": "Thompson",
    "Type": "Racetrack",
    "Surface": "Mixed",
    "Status": "Temporary"
  },
  "26": {
    "Track": "Lee USA Speedway",
    "Date": "2017-07-21T04:00:00.000Z",
    "State": "NH",
    "City": "Lee",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.375,
    "Latitude": 43.115867,
    "Longitude": -71.039733,
    "Status": "Permanent"
  },
  "27": {
    "Track": "Albany-Saratoga Speedway",
    "Date": "2017-07-28T04:00:00.000Z",
    "State": "NY",
    "City": "Malta",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 42.988542,
    "Longitude": -73.78216,
    "Status": "Permanent"
  },
  "28": {
    "Track": "New London Waterford Speedbowl",
    "Date": "2017-08-12T04:00:00.000Z",
    "State": "CT",
    "City": "Waterford",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.375,
    "Latitude": 41.396765,
    "Longitude": -72.17621,
    "Status": "Permanent"
  },
  "29": {
    "Track": "Oxford Plains Speedway",
    "Date": "2017-08-27T04:00:00.000Z",
    "State": "ME",
    "City": "Oxford",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.375,
    "Latitude": 44.153846,
    "Longitude": -70.484541,
    "Status": "Permanent"
  },
  "30": {
    "Track": "Lebanon Valley Speedway",
    "Date": "2017-08-31T04:00:00.000Z",
    "State": "NY",
    "City": "West Lebanon",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 42.491995,
    "Longitude": -73.488908,
    "Status": "Permanent"
  },
  "31": {
    "Track": "Beech Ridge Speedway",
    "Date": "2017-09-17T04:00:00.000Z",
    "State": "ME",
    "City": "Scarborough",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.33,
    "Latitude": 43.610212,
    "Longitude": -70.380652,
    "Status": "Permanent"
  },
  "32": {
    "Track": "Wall Stadium Speedway",
    "Date": "2017-11-24T05:00:00.000Z",
    "State": "NJ",
    "City": "Wall",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.33,
    "Latitude": 40.175186,
    "Longitude": -74.115242,
    "Status": "Permanent"
  },
  "33": {
    "Track": "Wall Stadium Speedway (Inner Asphalt Oval)",
    "Date": "2017-11-25T05:00:00.000Z",
    "State": "NJ",
    "City": "Wall",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Status": "Permanent"
  },
  "34": {
    "Track": "Hudson Speedway",
    "Date": "2018-05-13T04:00:00.000Z",
    "State": "NH",
    "City": "Hudson",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 42.813592,
    "Longitude": -71.410685,
    "Status": "Permanent"
  },
  "35": {
    "Track": "Texas Motor Speedway",
    "Date": "2018-06-08T04:00:00.000Z",
    "State": "TX",
    "City": "Fort Worth",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 1.5,
    "Latitude": 33.036961,
    "Longitude": -97.281602,
    "Status": "Permanent"
  },
  "36": {
    "Track": "Lil' Texas Motor Speedway",
    "Date": "2018-06-08T04:00:00.000Z",
    "State": "TX",
    "City": "Fort Worth",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.2,
    "Latitude": 33.035957,
    "Longitude": -97.27588,
    "Status": "Permanent"
  },
  "37": {
    "Track": "Texas Motor Speedway (Asphalt Road Course)",
    "Date": "2018-06-09T04:00:00.000Z",
    "State": "TX",
    "City": "Fort Worth",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Status": "Temporary"
  },
  "38": {
    "Track": "Monadnock Speedway",
    "Date": "2018-07-07T04:00:00.000Z",
    "State": "NH",
    "City": "Winchester",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 42.831283,
    "Longitude": -72.362489,
    "Status": "Permanent"
  },
  "39": {
    "Track": "Stafford Motor Speedway (Inner Asphalt Oval)",
    "Date": "2018-07-27T04:00:00.000Z",
    "State": "CT",
    "City": "Stafford Springs",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Status": "Permanent"
  },
  "40": {
    "Track": "Bear Ridge Speedway",
    "Date": "2018-08-11T04:00:00.000Z",
    "State": "VT",
    "City": "Bradford",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 43.998119,
    "Longitude": -72.168196,
    "Status": "Permanent",
    "Character": "Oozing with Character"
  },
  "41": {
    "Track": "Devil's Bowl Speedway",
    "Date": "2018-09-16T04:00:00.000Z",
    "State": "VT",
    "City": "West Haven",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 43.667992,
    "Longitude": -73.294175,
    "Status": "Permanent"
  },
  "42": {
    "Track": "Lancaster Speedway",
    "Date": "2018-09-28T04:00:00.000Z",
    "State": "SC",
    "City": "Lancaster",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 34.779166,
    "Longitude": -80.78716,
    "Status": "Permanent"
  },
  "43": {
    "Track": "Charlotte Motor Speedway Roval",
    "Date": "2018-09-29T04:00:00.000Z",
    "State": "NC",
    "City": "Concord",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 2.28,
    "Latitude": 35.352002,
    "Longitude": -80.683515,
    "Status": "Permanent"
  },
  "44": {
    "Track": "Gateway Dirt Nationals",
    "Date": "2018-11-29T05:00:00.000Z",
    "State": "MO",
    "City": "St. Louis",
    "Type": "Arena",
    "Surface": "Dirt",
    "Length": 0.2,
    "Latitude": 38.632739,
    "Longitude": -90.188636,
    "Status": "Temporary",
    "Character": "Oozing with Character"
  },
  "45": {
    "Track": "Cure Insurance Arena",
    "Date": "2018-12-15T05:00:00.000Z",
    "State": "NJ",
    "City": "Trenton",
    "Type": "Arena",
    "Surface": "Dirt",
    "Length": 0.125,
    "Latitude": 40.21272,
    "Longitude": -74.757592,
    "Status": "Temporary"
  },
  "46": {
    "Track": "Exposition Center",
    "Date": "2019-03-09T05:00:00.000Z",
    "State": "NY",
    "City": "Syracuse",
    "Type": "Arena",
    "Surface": "Concrete",
    "Length": 0.125,
    "Latitude": 43.074406,
    "Longitude": -76.221899,
    "Status": "Temporary"
  },
  "47": {
    "Track": "Lincoln Speedway",
    "Date": "2019-03-23T04:00:00.000Z",
    "State": "PA",
    "City": "Abbottstown",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 39.870591,
    "Longitude": -76.994714,
    "Status": "Permanent"
  },
  "48": {
    "Track": "Port Royal Speedway",
    "Date": "2019-03-24T04:00:00.000Z",
    "State": "PA",
    "City": "Port Royal",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 40.535688,
    "Longitude": -77.389519,
    "Status": "Permanent"
  },
  "49": {
    "Track": "Orange County Fair Speedway",
    "Date": "2019-04-13T04:00:00.000Z",
    "State": "NY",
    "City": "Middletown",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.625,
    "Latitude": 41.447578,
    "Longitude": -74.393426,
    "Status": "Permanent"
  },
  "50": {
    "Track": "New Egypt Speedway",
    "Date": "2019-05-04T04:00:00.000Z",
    "State": "NJ",
    "City": "Plumsted",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.4375,
    "Latitude": 40.070578,
    "Longitude": -74.467841,
    "Status": "Permanent"
  },
  "51": {
    "Track": "Glen Ridge Motorsports Park",
    "Date": "2019-06-02T04:00:00.000Z",
    "State": "NY",
    "City": "Fultonville",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 42.933938,
    "Longitude": -74.4051,
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "52": {
    "Track": "Utica-Rome Speedway",
    "Date": "2019-07-07T04:00:00.000Z",
    "State": "NY",
    "City": "Vernon",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 43.078706,
    "Longitude": -75.516282,
    "Status": "Permanent"
  },
  "53": {
    "Track": "Thunder Road International Speedbowl",
    "Date": "2019-07-18T04:00:00.000Z",
    "State": "VT",
    "City": "Barre",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 44.179899,
    "Longitude": -72.487877,
    "Status": "Permanent"
  },
  "54": {
    "Track": "NHMS Flat Track",
    "Date": "2019-07-19T04:00:00.000Z",
    "State": "NH",
    "City": "Loudon",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 43.34798,
    "Longitude": -71.463928,
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "55": {
    "Track": "Meridian Speedway",
    "Date": "2019-07-27T04:00:00.000Z",
    "State": "ID",
    "City": "Meridian",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 43.601855,
    "Longitude": -116.390666,
    "Status": "Permanent"
  },
  "56": {
    "Track": "Slinger Speedway",
    "Date": "2019-08-04T04:00:00.000Z",
    "State": "WI",
    "City": "Slinger",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 43.340632,
    "Longitude": -88.277351,
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "57": {
    "Track": "Slinger Speedway (Asphalt Figure 8)",
    "Date": "2019-08-04T04:00:00.000Z",
    "State": "WI",
    "City": "Slinger",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Status": "Permanent"
  },
  "58": {
    "Track": "Slinger Speedway (Asphalt Road Course)",
    "Date": "2019-08-04T04:00:00.000Z",
    "State": "WI",
    "City": "Slinger",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Status": "Permanent"
  },
  "59": {
    "Track": "Southern Iowa Speedway",
    "Date": "2019-08-05T04:00:00.000Z",
    "State": "IA",
    "City": "Oskaloosa",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 41.303158,
    "Longitude": -92.657883,
    "Status": "Permanent"
  },
  "60": {
    "Track": "Knoxville Raceway",
    "Date": "2019-08-07T04:00:00.000Z",
    "State": "IA",
    "City": "Knoxville",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 41.326589,
    "Longitude": -93.111788,
    "Status": "Permanent"
  },
  "61": {
    "Track": "Proctor Speedway",
    "Date": "2019-08-11T04:00:00.000Z",
    "State": "MN",
    "City": "Proctor",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 46.750912,
    "Longitude": -92.214314,
    "Status": "Permanent"
  },
  "62": {
    "Track": "William's Grove Speedway",
    "Date": "2019-08-23T04:00:00.000Z",
    "State": "PA",
    "City": "Mechanicsburg",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 40.155486,
    "Longitude": -77.033648,
    "Status": "Permanent"
  },
  "63": {
    "Track": "BAPS Motor Speedway",
    "Date": "2019-08-25T04:00:00.000Z",
    "State": "PA",
    "City": "York Haven",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 40.112489,
    "Longitude": -76.825789,
    "Status": "Permanent"
  },
  "64": {
    "Track": "Seekonk Speedway (Asphalt Road Course)",
    "Date": "2019-08-31T04:00:00.000Z",
    "State": "MA",
    "City": "Seekonk",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Status": "Permanent"
  },
  "65": {
    "Track": "Eldora Speedway",
    "Date": "2019-09-28T04:00:00.000Z",
    "State": "OH",
    "City": "New Weston",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 40.318608,
    "Longitude": -84.633776,
    "Status": "Permanent"
  },
  "66": {
    "Track": "PPL Center",
    "Date": "2020-01-04T05:00:00.000Z",
    "State": "PA",
    "City": "Allentown",
    "Type": "Arena",
    "Surface": "Concrete",
    "Length": 0.175,
    "Latitude": 40.602711,
    "Longitude": -75.473078,
    "Status": "Temporary"
  },
  "67": {
    "Track": "Riverside Speedway",
    "Date": "2020-01-18T05:00:00.000Z",
    "State": "NH",
    "City": "Northumberland",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 44.596926,
    "Longitude": -71.542518,
    "Status": "Permanent"
  },
  "68": {
    "Track": "Boardwalk Hall",
    "Date": "2020-02-01T05:00:00.000Z",
    "State": "NJ",
    "City": "Atlantic City",
    "Type": "Arena",
    "Surface": "Concrete",
    "Length": 0.175,
    "Latitude": 39.355096,
    "Longitude": -74.438648,
    "Recap": "x",
    "Status": "Temporary"
  },
  "69": {
    "Track": "Paragon Speedway",
    "Date": "2020-06-16T04:00:00.000Z",
    "State": "IN",
    "City": "Paragon",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 39.391225,
    "Longitude": -86.587073,
    "Recap": "x",
    "Status": "Permanent"
  },
  "70": {
    "Track": "Gas City Speedway",
    "Date": "2020-06-17T04:00:00.000Z",
    "State": "IN",
    "City": "Gas City",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 40.483466,
    "Longitude": -85.563242,
    "Status": "Permanent"
  },
  "71": {
    "Track": "Lincoln Park Speedway",
    "Date": "2020-06-18T04:00:00.000Z",
    "State": "IN",
    "City": "Greencastle",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.3125,
    "Latitude": 39.57626,
    "Longitude": -86.869947,
    "Status": "Permanent"
  },
  "72": {
    "Track": "Tri-State Speedway",
    "Date": "2020-06-19T04:00:00.000Z",
    "State": "IN",
    "City": "Haubstadt",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 38.205983,
    "Longitude": -87.553621,
    "Recap": "x",
    "Status": "Permanent"
  },
  "73": {
    "Track": "Lawrenceburg Speedway",
    "Date": "2020-06-20T04:00:00.000Z",
    "State": "IN",
    "City": "Lawrenceburg",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 39.104738,
    "Longitude": -84.856087,
    "Status": "Permanent"
  },
  "74": {
    "Track": "Kokomo Speedway",
    "Date": "2020-06-21T04:00:00.000Z",
    "State": "IN",
    "City": "Kokomo",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 40.51123,
    "Longitude": -86.143393,
    "Status": "Permanent"
  },
  "75": {
    "Track": "Claremont Motorsports Park",
    "Date": "2020-06-26T04:00:00.000Z",
    "State": "NH",
    "City": "Claremont",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.33,
    "Latitude": 43.392067,
    "Longitude": -72.352005,
    "Status": "Permanent"
  },
  "76": {
    "Track": "Selinsgrove Speedway",
    "Date": "2020-06-28T04:00:00.000Z",
    "State": "PA",
    "City": "Selinsgrove",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 40.787057,
    "Longitude": -76.870238,
    "Status": "Permanent"
  },
  "77": {
    "Track": "Grandview Speedway",
    "Date": "2020-06-30T04:00:00.000Z",
    "State": "PA",
    "City": "Bechtelsville",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 40.372544,
    "Longitude": -75.610115,
    "Status": "Permanent"
  },
  "78": {
    "Track": "Hagerstown Speedway",
    "Date": "2020-07-02T04:00:00.000Z",
    "State": "MD",
    "City": "Hagerstown",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 39.660672,
    "Longitude": -77.843921,
    "Status": "Permanent"
  },
  "79": {
    "Track": "Big Diamond Speedway",
    "Date": "2020-07-03T04:00:00.000Z",
    "State": "PA",
    "City": "Minersville",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 40.684617,
    "Longitude": -76.303246,
    "Recap": "x",
    "Status": "Permanent"
  },
  "80": {
    "Track": "White Mountain Motorsports Park",
    "Date": "2020-07-04T04:00:00.000Z",
    "State": "NH",
    "City": "North Woodstock",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 44.006522,
    "Longitude": -71.681925,
    "Recap": "x",
    "Status": "Permanent"
  },
  "81": {
    "Track": "Londonderry Speedway",
    "Date": "2020-08-01T04:00:00.000Z",
    "State": "NH",
    "City": "Londonderry",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 42.920848,
    "Longitude": -71.414851,
    "Recap": "x",
    "Status": "Permanent"
  },
  "82": {
    "Track": "Legion Speedway",
    "Date": "2020-08-01T04:00:00.000Z",
    "State": "NH",
    "City": "Rumney",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 43.818725,
    "Longitude": -71.8937,
    "Status": "Permanent"
  },
  "83": {
    "Track": "Lucas Oil Raceway",
    "Date": "2020-08-21T04:00:00.000Z",
    "State": "IN",
    "City": "Brownsburg",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.686,
    "Latitude": 39.812582,
    "Longitude": -86.340586,
    "Recap": "x",
    "Status": "Permanent"
  },
  "84": {
    "Track": "Lucas Oil Speedway Off Road Course",
    "Date": "2020-08-22T04:00:00.000Z",
    "State": "MO",
    "City": "Wheatland",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 1.3,
    "Latitude": 37.936849,
    "Longitude": -93.392579,
    "Status": "Permanent"
  },
  "85": {
    "Track": "Lucas Oil Speedway",
    "Date": "2020-08-22T04:00:00.000Z",
    "State": "MO",
    "City": "Wheatland",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 37.940222,
    "Longitude": -93.397699,
    "Status": "Permanent"
  },
  "86": {
    "Track": "Indiana State Fairgrounds",
    "Date": "2020-08-23T04:00:00.000Z",
    "State": "IN",
    "City": "Indianapolis",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 1,
    "Latitude": 39.829557,
    "Longitude": -86.134228,
    "Recap": "x",
    "Status": "Permanent"
  },
  "87": {
    "Track": "Gateway Motorsports Park",
    "Date": "2020-08-29T04:00:00.000Z",
    "State": "IL",
    "City": "Madison",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 1.25,
    "Latitude": 38.651483,
    "Longitude": -90.135503,
    "Status": "Permanent"
  },
  "88": {
    "Track": "Macon Speedway",
    "Date": "2020-08-29T04:00:00.000Z",
    "State": "IL",
    "City": "Macon",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.2,
    "Latitude": 39.712101,
    "Longitude": -89.006834,
    "Status": "Permanent"
  },
  "89": {
    "Track": "New Hampshire Motor Speedway (Asphalt Legends Oval)",
    "Date": "2020-09-12T04:00:00.000Z",
    "State": "NH",
    "City": "Loudon",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "90": {
    "Track": "Bridgeport Motorsports Park",
    "Date": "2020-11-06T05:00:00.000Z",
    "State": "NJ",
    "City": "Swedesboro",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Latitude": 39.819307,
    "Longitude": -75.317575,
    "Status": "Permanent"
  },
  "91": {
    "Track": "Lee Pond",
    "Date": "2021-01-31T05:00:00.000Z",
    "State": "NH",
    "City": "Moultonborough",
    "Type": "Lake",
    "Surface": "Ice",
    "Latitude": 43.7416295733249,
    "Longitude": -71.3972113377312,
    "Recap": "x",
    "Status": "Temporary"
  },
  "92": {
    "Track": "Berry Pond",
    "Date": "2021-02-06T05:00:00.000Z",
    "State": "NH",
    "City": "Moultonborough",
    "Type": "Lake",
    "Surface": "Ice",
    "Latitude": 43.7588525295176,
    "Longitude": -71.3935907924762,
    "Status": "Temporary"
  },
  "93": {
    "Track": "Northeast Pond",
    "Date": "2021-02-07T05:00:00.000Z",
    "State": "NH",
    "City": "Milton",
    "Type": "Lake",
    "Surface": "Ice",
    "Latitude": 43.4442995517814,
    "Longitude": -70.9636735387532,
    "Status": "Temporary"
  },
  "94": {
    "Track": "Contoocook Lake",
    "Date": "2021-02-14T05:00:00.000Z",
    "State": "NH",
    "City": "Jaffrey",
    "Type": "Lake",
    "Surface": "Ice",
    "Latitude": 42.7955399320377,
    "Longitude": -72.0077349892875,
    "Status": "Temporary"
  },
  "95": {
    "Track": "Rochester Fairgrounds",
    "Date": "2021-03-06T05:00:00.000Z",
    "State": "NH",
    "City": "Rochester",
    "Type": "Fair",
    "Surface": "Dirt",
    "Latitude": 43.2969490477573,
    "Longitude": -70.9832266862897,
    "Recap": "x",
    "Status": "Temporary"
  },
  "96": {
    "Track": "Bristol Motor Speedway (Dirt)",
    "Date": "2021-03-19T04:00:00.000Z",
    "State": "TN",
    "City": "Bristol",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 36.5155905074463,
    "Longitude": -82.2571598217224,
    "Status": "Permanent"
  },
  "97": {
    "Track": "Mountain Creek Speedway",
    "Date": "2021-03-21T04:00:00.000Z",
    "State": "NC",
    "City": "Catawba",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.16,
    "Latitude": 35.6047121721003,
    "Longitude": -81.0757647727015,
    "Status": "Permanent"
  },
  "98": {
    "Track": "Millbridge Speedway",
    "Date": "2021-03-23T04:00:00.000Z",
    "State": "NC",
    "City": "Salisbury",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.16,
    "Latitude": 35.6533176141607,
    "Longitude": -80.6081584281256,
    "Status": "Permanent"
  },
  "99": {
    "Track": "Boyd's Speedway",
    "Date": "2021-03-26T04:00:00.000Z",
    "State": "GA",
    "City": "Ringgold",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 34.9847781036773,
    "Longitude": -85.1945374800083,
    "Recap": "x",
    "Status": "Permanent"
  },
  "100": {
    "Track": "Fonda Speedway",
    "Date": "2021-04-18T04:00:00.000Z",
    "State": "NY",
    "City": "Fonda",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 42.9522323308999,
    "Longitude": -74.3674486590383,
    "Status": "Permanent"
  },
  "101": {
    "Track": "Rochester Fairgrounds (Dirt Road Course)",
    "Date": "2021-05-08T04:00:00.000Z",
    "State": "NH",
    "City": "Rochester",
    "Type": "Fair",
    "Surface": "Dirt",
    "Recap": "x",
    "Status": "Temporary"
  },
  "102": {
    "Track": "Central Cycle Club",
    "Date": "2021-05-23T04:00:00.000Z",
    "State": "CT",
    "City": "Central Village",
    "Type": "Motocross",
    "Surface": "Dirt",
    "Latitude": 41.7211615227574,
    "Longitude": -71.9230246254887,
    "Recap": "x",
    "Status": "Permanent"
  },
  "103": {
    "Track": "Pomfret Speedway",
    "Date": "2021-05-23T04:00:00.000Z",
    "State": "CT",
    "City": "Pomfret",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.125,
    "Latitude": 41.9013745954223,
    "Longitude": -71.9881088527105,
    "Recap": "x",
    "Status": "Permanent"
  },
  "104": {
    "Track": "Fulton Speedway",
    "Date": "2021-05-29T04:00:00.000Z",
    "State": "NY",
    "City": "Fulton",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 43.2805236120949,
    "Longitude": -76.383604336207,
    "Recap": "x",
    "Status": "Permanent"
  },
  "105": {
    "Track": "Action Track USA",
    "Date": "2021-06-13T04:00:00.000Z",
    "State": "PA",
    "City": "Kutztown",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.2,
    "Latitude": 40.5161840133541,
    "Longitude": -75.7831989072972,
    "Recap": "x",
    "Status": "Permanent"
  },
  "106": {
    "Track": "Wayne County Speedway",
    "Date": "2021-06-14T04:00:00.000Z",
    "State": "OH",
    "City": "Orrville",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 40.810438439051,
    "Longitude": -81.7821935585399,
    "Recap": "x",
    "Status": "Permanent"
  },
  "107": {
    "Track": "Path Valley Speedway Park",
    "Date": "2021-06-19T04:00:00.000Z",
    "State": "PA",
    "City": "Spring Run",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 40.1645496520505,
    "Longitude": -77.7836609426681,
    "Recap": "x",
    "Status": "Permanent"
  },
  "108": {
    "Track": "Selinsgrove Raceway Park",
    "Date": "2021-06-20T04:00:00.000Z",
    "State": "PA",
    "City": "Selinsgrove",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.2,
    "Latitude": 40.7869677307743,
    "Longitude": -76.8703099980556,
    "Recap": "x",
    "Status": "Permanent"
  },
  "109": {
    "Track": "Bloomsburg Fairgrounds Speedway",
    "Date": "2021-06-20T04:00:00.000Z",
    "State": "PA",
    "City": "Bloomsburg",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 40.9963649758338,
    "Longitude": -76.4641344600989,
    "Recap": "x",
    "Status": "Permanent"
  },
  "110": {
    "Track": "Riverhead Raceway",
    "Date": "2021-06-26T04:00:00.000Z",
    "State": "NY",
    "City": "Riverhead",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 40.9224923000117,
    "Longitude": -72.7045220371278,
    "Recap": "x",
    "Status": "Permanent"
  },
  "111": {
    "Track": "Riverhead Raceway (Asphalt Figure 8)",
    "Date": "2021-06-26T04:00:00.000Z",
    "State": "NY",
    "City": "Riverhead",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "112": {
    "Track": "KRA Speedway",
    "Date": "2021-07-08T04:00:00.000Z",
    "State": "MN",
    "City": "Willmar",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 45.1300012335653,
    "Longitude": -95.0559613582346,
    "Recap": "x",
    "Status": "Permanent"
  },
  "113": {
    "Track": "ERX Motor Park",
    "Date": "2021-07-10T04:00:00.000Z",
    "State": "MN",
    "City": "Elk River",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.85,
    "Latitude": 45.3621084965766,
    "Longitude": -93.55824078866,
    "Recap": "x",
    "Status": "Permanent"
  },
  "114": {
    "Track": "Mason City Motor Speedway",
    "Date": "2021-07-11T04:00:00.000Z",
    "State": "IA",
    "City": "Mason City",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 43.1537371391555,
    "Longitude": -93.2559507034742,
    "Recap": "x",
    "Status": "Permanent"
  },
  "115": {
    "Track": "Clyde Martin Memorial Speedway",
    "Date": "2021-08-07T04:00:00.000Z",
    "State": "PA",
    "City": "Newmanstown",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.175,
    "Latitude": 40.2751593797983,
    "Longitude": -76.2585880193477,
    "Recap": "x",
    "Status": "Permanent"
  },
  "116": {
    "Track": "Perris Auto Speeedway",
    "Date": "2021-08-21T04:00:00.000Z",
    "State": "CA",
    "City": "Perris",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.4,
    "Latitude": 33.8494502339255,
    "Longitude": -117.201095674817,
    "Recap": "x",
    "Status": "Permanent"
  },
  "117": {
    "Track": "Huset's Speedway",
    "Date": "2021-09-10T04:00:00.000Z",
    "State": "SD",
    "City": "Brandon",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 43.5706706230416,
    "Longitude": -96.5835316608866,
    "Recap": "x",
    "Status": "Permanent"
  },
  "118": {
    "Track": "Talladega Superspeedway",
    "Date": "2021-10-02T04:00:00.000Z",
    "State": "AL",
    "City": "Talladega",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 2.66,
    "Latitude": 33.5673049488553,
    "Longitude": -86.0669514222237,
    "Recap": "x",
    "Status": "Permanent"
  },
  "119": {
    "Track": "Talladega Short Track",
    "Date": "2021-10-02T04:00:00.000Z",
    "State": "AL",
    "City": "Talladega",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 33.5815423553349,
    "Longitude": -86.0514625156166,
    "Recap": "x",
    "Status": "Permanent"
  },
  "120": {
    "Track": "Topsfield Fair Arena",
    "Date": "2021-10-11T04:00:00.000Z",
    "State": "MA",
    "City": "Topsfield",
    "Type": "Fair",
    "Surface": "Dirt",
    "Latitude": 42.6283272037037,
    "Longitude": -70.943103123818,
    "Recap": "x",
    "Status": "Temporary"
  },
  "121": {
    "Track": "Arizona Speedway",
    "Date": "2021-11-12T05:00:00.000Z",
    "State": "AZ",
    "City": "San Tan Valley",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 33.3115230490482,
    "Longitude": -111.565865280717,
    "Recap": "x",
    "Status": "Permanent"
  },
  "122": {
    "Track": "Wild Horse Pass Motorsports Park (Short Course)",
    "Date": "2021-11-13T05:00:00.000Z",
    "State": "AZ",
    "City": "Chandler",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Status": "Permanent"
  },
  "123": {
    "Track": "Wild Horse Pass Motorsports Park",
    "Date": "2021-11-14T05:00:00.000Z",
    "State": "AZ",
    "City": "Chandler",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Latitude": 33.264085330606,
    "Longitude": -111.958944419759,
    "Status": "Permanent"
  },
  "124": {
    "Track": "Glen Helen Raceway",
    "Date": "2021-11-20T05:00:00.000Z",
    "State": "CA",
    "City": "San Bernardino",
    "Type": "Racetrack",
    "Surface": "Mixed",
    "Length": 0.48,
    "Latitude": 34.1887632910539,
    "Longitude": -117.386511402105,
    "Status": "Permanent"
  },
  "125": {
    "Track": "Perris Auto Speeedway (Dirt Figure 8)",
    "Date": "2021-11-20T05:00:00.000Z",
    "State": "CA",
    "City": "Perris",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "126": {
    "Track": "Perris Auto Speeedway (Inner Dirt Oval)",
    "Date": "2021-11-20T05:00:00.000Z",
    "State": "CA",
    "City": "Perris",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "127": {
    "Track": "Perris Auto Speeedway (Dirt Road Course)",
    "Date": "2021-11-20T05:00:00.000Z",
    "State": "CA",
    "City": "Perris",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "128": {
    "Track": "Cocopah Speedway",
    "Date": "2022-01-27T05:00:00.000Z",
    "State": "AZ",
    "City": "Somerton",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 32.6159828658144,
    "Longitude": -114.655874736883,
    "Recap": "x",
    "Status": "Permanent"
  },
  "129": {
    "Track": "Irwindale Speedway",
    "Date": "2022-02-05T05:00:00.000Z",
    "State": "CA",
    "City": "Irwindale",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.5,
    "Latitude": 34.1095399082674,
    "Longitude": -117.987927624045,
    "Recap": "x",
    "Status": "Permanent"
  },
  "130": {
    "Track": "Los Angeles Memorial Coliseum",
    "Date": "2022-02-06T05:00:00.000Z",
    "State": "CA",
    "City": "Los Angeles",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 34.014011457585,
    "Longitude": -118.287945146258,
    "Recap": "x",
    "Status": "Temporary"
  },
  "131": {
    "Track": "Hickory Motor Speedway",
    "Date": "2022-03-18T04:00:00.000Z",
    "State": "NC",
    "City": "Newton",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.375,
    "Latitude": 35.6957687910595,
    "Longitude": -81.2693514012835,
    "Recap": "x",
    "Status": "Permanent"
  },
  "132": {
    "Track": "Carolina Speedway",
    "Date": "2022-03-18T04:00:00.000Z",
    "State": "NC",
    "City": "Gastonia",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.4,
    "Latitude": 35.1720897678417,
    "Longitude": -81.1080438622015,
    "Recap": "x",
    "Status": "Permanent"
  },
  "133": {
    "Track": "Atlanta Motor Speedway",
    "Date": "2022-03-19T04:00:00.000Z",
    "State": "GA",
    "City": "Hampton",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 1.54,
    "Latitude": 33.3835077297094,
    "Longitude": -84.3178574551298,
    "Status": "Permanent"
  },
  "134": {
    "Track": "Senoia Raceway",
    "Date": "2022-03-19T04:00:00.000Z",
    "State": "GA",
    "City": "Senoia",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 33.3057636660791,
    "Longitude": -84.5898389294192,
    "Status": "Permanent"
  },
  "135": {
    "Track": "Cherokee Speedway",
    "Date": "2022-03-26T04:00:00.000Z",
    "State": "SC",
    "City": "Gaffney",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 35.1079485084983,
    "Longitude": -81.5977816529613,
    "Recap": "x",
    "Status": "Permanent"
  },
  "136": {
    "Track": "Ventura Raceway",
    "Date": "2022-06-11T04:00:00.000Z",
    "State": "CA",
    "City": "Ventura",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.2,
    "Latitude": 34.2755527364598,
    "Longitude": -119.304332771755,
    "Recap": "x",
    "Status": "Permanent"
  },
  "137": {
    "Track": "Bakersfield Speedway [Inner Dirt Oval]",
    "Date": "2022-06-18T04:00:00.000Z",
    "State": "CA",
    "City": "Bakersfield",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.1,
    "Recap": "x",
    "Status": "Permanent"
  },
  "138": {
    "Track": "Kern County Raceway Park",
    "Date": "2022-06-18T04:00:00.000Z",
    "State": "CA",
    "City": "Bakersfield",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.5,
    "Latitude": 35.2927692438009,
    "Longitude": -119.256255030109,
    "Recap": "x",
    "Status": "Permanent"
  },
  "139": {
    "Track": "Cottage Grove Speedway",
    "Date": "2022-06-21T04:00:00.000Z",
    "State": "OR",
    "City": "Cottage Grove",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 43.8110011883976,
    "Longitude": -123.045621052352,
    "Status": "Permanent"
  },
  "140": {
    "Track": "Skagit Speedway",
    "Date": "2022-06-23T04:00:00.000Z",
    "State": "WA",
    "City": "Skagit",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.3,
    "Latitude": 48.576525406898,
    "Longitude": -122.332882347983,
    "Recap": "x",
    "Status": "Permanent"
  },
  "141": {
    "Track": "Greenwood Valley Action Tracks",
    "Date": "2022-07-18T04:00:00.000Z",
    "State": "PA",
    "City": "Orangeville",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.2,
    "Latitude": 41.1193145331075,
    "Longitude": -76.4622813201344,
    "Recap": "x",
    "Status": "Permanent"
  },
  "142": {
    "Track": "Spirit Auto Center Speedway",
    "Date": "2022-07-19T04:00:00.000Z",
    "State": "NJ",
    "City": "Swedesboro",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Status": "Permanent"
  },
  "143": {
    "Track": "Shellhammer Dirt Track",
    "Date": "2022-07-20T04:00:00.000Z",
    "State": "PA",
    "City": "Shoemakersville",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.125,
    "Latitude": 40.4632998294636,
    "Longitude": -75.9745481579341,
    "Status": "Permanent"
  },
  "144": {
    "Track": "Linda's Speedway",
    "Date": "2022-07-21T04:00:00.000Z",
    "State": "PA",
    "City": "Jonestown",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 40.427578451762,
    "Longitude": -76.506823276096,
    "Recap": "x",
    "Status": "Permanent"
  },
  "145": {
    "Track": "Iowa Speedway",
    "Date": "2022-07-23T04:00:00.000Z",
    "State": "IA",
    "City": "Newton",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.875,
    "Latitude": 41.6745668213037,
    "Longitude": -93.0133531174115,
    "Status": "Permanent"
  },
  "146": {
    "Track": "Boone Speedway",
    "Date": "2022-07-23T04:00:00.000Z",
    "State": "IA",
    "City": "Boone",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 42.0324339176541,
    "Longitude": -93.8767120037113,
    "Status": "Permanent"
  },
  "147": {
    "Track": "Benton County Speedway",
    "Date": "2022-07-24T04:00:00.000Z",
    "State": "IA",
    "City": "Vinton",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 42.1544758904535,
    "Longitude": -92.0192253830214,
    "Status": "Permanent"
  },
  "148": {
    "Track": "Circle City Raceway",
    "Date": "2022-07-25T04:00:00.000Z",
    "State": "IN",
    "City": "Indianapolis",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 39.7311048205333,
    "Longitude": -86.0383863331974,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "149": {
    "Track": "Pendleton County Fairgrounds",
    "Date": "2022-07-27T04:00:00.000Z",
    "State": "KY",
    "City": "Falmouth",
    "Type": "Fair",
    "Surface": "Dirt",
    "Latitude": 38.6736910779316,
    "Longitude": -84.3429424019852,
    "Recap": "x",
    "Status": "Temporary"
  },
  "150": {
    "Track": "Bloomington Speedway",
    "Date": "2022-07-29T04:00:00.000Z",
    "State": "IN",
    "City": "Bloomington",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 39.1098246630204,
    "Longitude": -86.523009132091,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "151": {
    "Track": "Indianapolis Motor Speedway Road Course",
    "Date": "2022-07-30T04:00:00.000Z",
    "State": "IN",
    "City": "Speedway",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 2.439,
    "Latitude": 39.7951021823793,
    "Longitude": -86.2347219896014,
    "Status": "Permanent"
  },
  "152": {
    "Track": "Dirt City Motorplex",
    "Date": "2022-07-31T04:00:00.000Z",
    "State": "WI",
    "City": "Lena",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.7,
    "Latitude": 44.9567332889702,
    "Longitude": -88.033099675762,
    "Recap": "x",
    "Status": "Permanent"
  },
  "153": {
    "Track": "New Hampshire Motor Speedway [Asphalt Road Course - Full]",
    "Date": "2022-08-14T04:00:00.000Z",
    "State": "NH",
    "City": "Loudon",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 1.6,
    "Recap": "x",
    "Status": "Permanent"
  },
  "154": {
    "Track": "Outlaw Speedway",
    "Date": "2022-08-19T04:00:00.000Z",
    "State": "NY",
    "City": "Dundee",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 42.5150840422171,
    "Longitude": -76.9725809733495,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "155": {
    "Track": "Skyline Raceway Motorsports Park",
    "Date": "2022-08-20T04:00:00.000Z",
    "State": "NY",
    "City": "Virgil",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 42.5426472279978,
    "Longitude": -76.1168282537041,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "156": {
    "Track": "Thunder Mountain Speedway",
    "Date": "2022-08-20T04:00:00.000Z",
    "State": "NY",
    "City": "Lisle",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 42.3648652584672,
    "Longitude": -76.0726253549486,
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "157": {
    "Track": "Five Mile Point Speedway",
    "Date": "2022-08-20T04:00:00.000Z",
    "State": "NY",
    "City": "Five Mile Point",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 42.0921536456026,
    "Longitude": -75.8162609055216,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "158": {
    "Track": "I-30 Speedway",
    "Date": "2022-09-30T04:00:00.000Z",
    "State": "AR",
    "City": "Little Rock",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 34.640522874382,
    "Longitude": -92.4398092135323,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "159": {
    "Track": "Tri-County Race Track",
    "Date": "2022-10-06T04:00:00.000Z",
    "State": "NC",
    "City": "Brasstown",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 35.0332848680928,
    "Longitude": -83.9534497895667,
    "Recap": "x",
    "Status": "Permanent"
  },
  "160": {
    "Track": "Nashville Fairgrounds Speedway [Inner]",
    "Date": "2022-10-08T04:00:00.000Z",
    "State": "TN",
    "City": "Nashville",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Recap": "x",
    "Status": "Permanent"
  },
  "161": {
    "Track": "411 Motor Speedway",
    "Date": "2022-10-11T04:00:00.000Z",
    "State": "TN",
    "City": "Seymour",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 35.8597861727612,
    "Longitude": -83.7759310889283,
    "Recap": "x",
    "Status": "Permanent"
  },
  "162": {
    "Track": "Irwindale Speedway [Inner Asphalt Oval]",
    "Date": "2022-10-29T04:00:00.000Z",
    "State": "CA",
    "City": "Irwindale",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.33,
    "Status": "Permanent"
  },
  "163": {
    "Track": "Irwindale Speedway [Asphalt Figure-8]",
    "Date": "2022-10-29T04:00:00.000Z",
    "State": "CA",
    "City": "Irwindale",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Status": "Permanent"
  },
  "164": {
    "Track": "Adobe Mountain Speedway",
    "Date": "2022-11-12T05:00:00.000Z",
    "State": "AZ",
    "City": "Glendale",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.2,
    "Latitude": 33.6875265947298,
    "Longitude": -112.158191998534,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "165": {
    "Track": "Bakersfield Speedway",
    "Date": "2022-11-15T05:00:00.000Z",
    "State": "CA",
    "City": "Bakersfield",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 35.4514246435163,
    "Longitude": -119.028834815099,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "166": {
    "Track": "Southern Illinois Center",
    "Date": "2022-12-17T05:00:00.000Z",
    "State": "IL",
    "City": "Du Quoin",
    "Type": "Arena",
    "Surface": "Dirt",
    "Latitude": 37.9786431902449,
    "Longitude": -89.22665402517,
    "Recap": "x",
    "Status": "Temporary",
    "Character": "A Lot of Character"
  },
  "167": {
    "Track": "Tulsa Expo Raceway",
    "Date": "2023-01-09T05:00:00.000Z",
    "State": "OK",
    "City": "Tulsa",
    "Type": "Arena",
    "Surface": "Dirt",
    "Latitude": 36.1344417505393,
    "Longitude": -95.9325149211223,
    "Status": "Temporary"
  },
  "168": {
    "Track": "Circuit de Trois-Rivieres (Rallycross)",
    "Date": "2023-01-22T05:00:00.000Z",
    "State": "QC",
    "City": "Trois-Rivieres",
    "Type": "Road Course",
    "Surface": "Mixed",
    "Latitude": 46.3462336932727,
    "Longitude": -72.5594072408029,
    "Recap": "x",
    "Status": "Temporary"
  },
  "169": {
    "Track": "Marion County Speedway",
    "Date": "2023-02-08T05:00:00.000Z",
    "State": "FL",
    "City": "Ocala",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Latitude": 29.2629468043957,
    "Longitude": -82.1758988983068,
    "Status": "Permanent"
  },
  "170": {
    "Track": "Volusia Speedway Park",
    "Date": "2023-02-09T05:00:00.000Z",
    "State": "FL",
    "City": "De Leon Springs",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 29.2157045217781,
    "Longitude": -81.3442006912857,
    "Recap": "x",
    "Status": "Permanent"
  },
  "171": {
    "Track": "Auburndale Speedway",
    "Date": "2023-02-10T05:00:00.000Z",
    "State": "FL",
    "City": "Winter Haven",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 28.0316066607177,
    "Longitude": -81.7905987954891,
    "Recap": "x",
    "Status": "Permanent"
  },
  "172": {
    "Track": "Showtime Speedway",
    "Date": "2023-02-10T05:00:00.000Z",
    "State": "FL",
    "City": "Clearwater",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 27.8853348766403,
    "Longitude": -82.6896102093643,
    "Recap": "x",
    "Status": "Permanent"
  },
  "173": {
    "Track": "Showtime Speedway [Asphalt Figure-8]",
    "Date": "2023-02-10T05:00:00.000Z",
    "State": "FL",
    "City": "Clearwater",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "174": {
    "Track": "Hobe Sound Speedway",
    "Date": "2023-02-11T05:00:00.000Z",
    "State": "FL",
    "City": "Hobe Sound",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.15,
    "Latitude": 27.0390122232515,
    "Longitude": -80.1845623475864,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Minimal Character"
  },
  "175": {
    "Track": "Hendry County Motorsports Park",
    "Date": "2023-02-11T05:00:00.000Z",
    "State": "FL",
    "City": "Clewiston",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 26.7675563361621,
    "Longitude": -81.090152480741,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "176": {
    "Track": "New Smyrna Speedway",
    "Date": "2023-02-12T05:00:00.000Z",
    "State": "FL",
    "City": "New Smyrna Beach",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.5,
    "Latitude": 29.0136617297322,
    "Longitude": -81.0698479772792,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "177": {
    "Track": "East Bay Raceway Park",
    "Date": "2023-02-13T05:00:00.000Z",
    "State": "FL",
    "City": "Tampa",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 27.8840433324438,
    "Longitude": -82.3882248101782,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "178": {
    "Track": "Citrus County Speedway",
    "Date": "2023-02-16T05:00:00.000Z",
    "State": "FL",
    "City": "Inverness",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 28.8075818194467,
    "Longitude": -82.3152079722962,
    "Recap": "x",
    "Status": "Permanent"
  },
  "179": {
    "Track": "Ocala Raceway",
    "Date": "2023-02-16T05:00:00.000Z",
    "State": "FL",
    "City": "Ocala",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Latitude": 29.2823606666002,
    "Longitude": -82.1861741089833,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "180": {
    "Track": "Daytona International Speedway",
    "Date": "2023-02-17T05:00:00.000Z",
    "State": "FL",
    "City": "Daytona Beach",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 2.5,
    "Latitude": 29.1864522178763,
    "Longitude": -81.0710000722145,
    "Status": "Permanent"
  },
  "181": {
    "Track": "Auto Club Speedway",
    "Date": "2023-02-26T05:00:00.000Z",
    "State": "CA",
    "City": "Fontana",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 2,
    "Latitude": 34.0874873510594,
    "Longitude": -117.500664103446,
    "Status": "Permanent"
  },
  "182": {
    "Track": "Accord Speedway",
    "Date": "2023-05-09T04:00:00.000Z",
    "State": "NY",
    "City": "Accord",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 41.829144935152,
    "Longitude": -74.219986229365,
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "183": {
    "Track": "Clinton County Speedway",
    "Date": "2023-05-19T04:00:00.000Z",
    "State": "PA",
    "City": "Mill Hall",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 41.0653181455701,
    "Longitude": -77.4524902668935,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "184": {
    "Track": "North Wilkesboro Speedway",
    "Date": "2023-05-20T04:00:00.000Z",
    "State": "NC",
    "City": "North Wilkesboro",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.625,
    "Latitude": 36.142559719319,
    "Longitude": -81.072399491873,
    "Status": "Permanent",
    "Character": "Oozing with Character"
  },
  "185": {
    "Track": "Bowman Gray Stadium",
    "Date": "2023-05-20T04:00:00.000Z",
    "State": "NC",
    "City": "Winston-Salem",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 36.0827083481516,
    "Longitude": -80.2220055528193,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Oozing with Character"
  },
  "186": {
    "Track": "Wiscasset Speedway",
    "Date": "2023-05-28T04:00:00.000Z",
    "State": "ME",
    "City": "Wiscasset",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.375,
    "Latitude": 44.0388605887536,
    "Longitude": -69.6588949122878,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "187": {
    "Track": "Chicago Street Course",
    "Date": "2023-07-02T04:00:00.000Z",
    "State": "IL",
    "City": "Chicago",
    "Type": "Street",
    "Surface": "Asphalt",
    "Length": 2.2,
    "Latitude": 41.8732786482641,
    "Longitude": -87.6206507160898,
    "Recap": "x",
    "Status": "Temporary"
  },
  "188": {
    "Track": "Rockford Speedway",
    "Date": "2023-07-03T04:00:00.000Z",
    "State": "IL",
    "City": "Rockford",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Latitude": 42.3636111699981,
    "Longitude": -89.0176889545391,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "189": {
    "Track": "What Cheer Raceway [Dirt Oval]",
    "Date": "2023-07-04T04:00:00.000Z",
    "State": "IA",
    "City": "What Cheer",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.1,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "190": {
    "Track": "What Cheer Raceway",
    "Date": "2023-07-04T04:00:00.000Z",
    "State": "IA",
    "City": "What Cheer",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Latitude": 41.4095401551561,
    "Longitude": -92.3501225406632,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "191": {
    "Track": "Independence Motor Speedway",
    "Date": "2023-07-05T04:00:00.000Z",
    "State": "IA",
    "City": "Independence",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 42.4813372108022,
    "Longitude": -91.8930712905105,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "192": {
    "Track": "Farmer City Raceway",
    "Date": "2023-07-07T04:00:00.000Z",
    "State": "IL",
    "City": "Farmer City",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 40.2537863736406,
    "Longitude": -88.6392561914229,
    "Recap": "x",
    "Status": "Permanent"
  },
  "193": {
    "Track": "NHMX Flat Track",
    "Date": "2023-07-15T04:00:00.000Z",
    "State": "NH",
    "City": "Lempster",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.2,
    "Latitude": 43.1852058867595,
    "Longitude": -72.2044859113491,
    "Recap": "x",
    "Status": "Permanent"
  },
  "194": {
    "Track": "Pocono Raceway",
    "Date": "2023-07-23T04:00:00.000Z",
    "State": "PA",
    "City": "Long Pond",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 2.5,
    "Latitude": 41.0530274224296,
    "Longitude": -75.511114113931,
    "Recap": "x",
    "Status": "Permanent"
  },
  "195": {
    "Track": "Bedford Fairgrounds Speedway",
    "Date": "2023-08-11T04:00:00.000Z",
    "State": "PA",
    "City": "Bedford",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 40.023715070945,
    "Longitude": -78.5206198612763,
    "Status": "Permanent"
  },
  "196": {
    "Track": "Big Al's Race Track",
    "Date": "2023-08-12T04:00:00.000Z",
    "State": "PA",
    "City": "Dornsife",
    "Type": "Field",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 40.752060612261,
    "Longitude": -76.7498442827175,
    "Status": "Permanent"
  },
  "197": {
    "Track": "Berkeley County Fairgrounds",
    "Date": "2023-08-12T04:00:00.000Z",
    "State": "WV",
    "City": "Martinsburg",
    "Type": "Fair",
    "Surface": "Dirt",
    "Latitude": 39.4413898427331,
    "Longitude": -77.9137142031628,
    "Status": "Temporary"
  },
  "198": {
    "Track": "Winchester Speedway",
    "Date": "2023-08-12T04:00:00.000Z",
    "State": "VA",
    "City": "Winchester",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 39.1322716813865,
    "Longitude": -78.1331216774041,
    "Recap": "x",
    "Status": "Permanent"
  },
  "199": {
    "Track": "Oreville Kart Club",
    "Date": "2023-08-13T04:00:00.000Z",
    "State": "PA",
    "City": "Mertztown",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.15,
    "Latitude": 40.5212014869911,
    "Longitude": -75.6895618671869,
    "Status": "Permanent"
  },
  "200": {
    "Track": "Evergreen Raceway",
    "Date": "2023-08-13T04:00:00.000Z",
    "State": "PA",
    "City": "Drums",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.33,
    "Latitude": 41.0252699304842,
    "Longitude": -76.000453128114,
    "Status": "Permanent"
  },
  "201": {
    "Track": "Marshfield Fair",
    "Date": "2023-08-26T04:00:00.000Z",
    "State": "MA",
    "City": "Marshfield",
    "Type": "Fair",
    "Surface": "Dirt",
    "Latitude": 42.0988191622504,
    "Longitude": -70.7162934982453,
    "Recap": "x",
    "Status": "Temporary"
  },
  "202": {
    "Track": "Unity Raceway",
    "Date": "2023-09-29T04:00:00.000Z",
    "State": "ME",
    "City": "Unity",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Latitude": 44.6119327344562,
    "Longitude": -69.3496438022345,
    "Recap": "x",
    "Status": "Permanent"
  },
  "203": {
    "Track": "Thompson Speedway [Asphalt Road Course]",
    "Date": "2023-09-30T04:00:00.000Z",
    "State": "CT",
    "City": "Thompson",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 1.7,
    "Recap": "x",
    "Status": "Permanent"
  },
  "204": {
    "Track": "Devil's Bowl Speedway (TX)",
    "Date": "2023-10-20T04:00:00.000Z",
    "State": "TX",
    "City": "Mesquite",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Latitude": 32.7379706162804,
    "Longitude": -96.5276391590924,
    "Recap": "x",
    "Status": "Permanent"
  },
  "205": {
    "Track": "Hudson Speedway [Asphalt Figure-8]",
    "Date": "2023-10-22T04:00:00.000Z",
    "State": "NH",
    "City": "Hudson",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Status": "Permanent"
  },
  "206": {
    "Track": "Stockton Dirt Track",
    "Date": "2023-11-04T04:00:00.000Z",
    "State": "CA",
    "City": "Stockton",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.4,
    "Latitude": 37.9384548724623,
    "Longitude": -121.261978101818,
    "Recap": "x",
    "Status": "Permanent"
  },
  "207": {
    "Track": "SBC Fairgrounds",
    "Date": "2023-11-05T04:00:00.000Z",
    "State": "CA",
    "City": "Victorville",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Latitude": 34.5223221509007,
    "Longitude": -117.311235918136,
    "Recap": "x",
    "Status": "Permanent"
  },
  "208": {
    "Track": "Wild Horse Pass Motorsports Park [Mixed Full Course]",
    "Date": "2023-11-10T05:00:00.000Z",
    "State": "AZ",
    "City": "Chandler",
    "Type": "Racetrack",
    "Surface": "Mixed",
    "Status": "Permanent"
  },
  "209": {
    "Track": "Wild Horse Pass Motorsports Park [Mixed Short Course]",
    "Date": "2023-11-10T05:00:00.000Z",
    "State": "AZ",
    "City": "Chandler",
    "Type": "Racetrack",
    "Surface": "Mixed",
    "Status": "Permanent"
  },
  "210": {
    "Track": "Central Arizona Raceway",
    "Date": "2023-11-10T05:00:00.000Z",
    "State": "AZ",
    "City": "Casa Grande",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Latitude": 32.8705170631656,
    "Longitude": -111.57081038944,
    "Recap": "x",
    "Status": "Permanent"
  },
  "211": {
    "Track": "Podium Club at Attesa (Full)",
    "Date": "2023-11-11T05:00:00.000Z",
    "State": "AZ",
    "City": "Casa Grande",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 2.32,
    "Latitude": 32.8165317597523,
    "Longitude": -111.832851496199,
    "Recap": "x",
    "Status": "Permanent"
  },
  "212": {
    "Track": "Shorty's Sports Park",
    "Date": "2023-11-12T05:00:00.000Z",
    "State": "CA",
    "City": "Blythe",
    "Type": "Motocross",
    "Surface": "Dirt",
    "Latitude": 33.6965018554679,
    "Longitude": -114.60617378652,
    "Recap": "x",
    "Status": "Permanent"
  },
  "213": {
    "Track": "Placerville Speedway",
    "Date": "2023-11-17T05:00:00.000Z",
    "State": "CA",
    "City": "Placerville",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 38.7261617914795,
    "Longitude": -120.832274490763,
    "Recap": "x",
    "Status": "Permanent"
  },
  "214": {
    "Track": "Merced Speedway",
    "Date": "2023-11-21T05:00:00.000Z",
    "State": "CA",
    "City": "Merced",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Latitude": 37.2911134785598,
    "Longitude": -120.482490466735,
    "Recap": "x",
    "Status": "Permanent"
  },
  "215": {
    "Track": "The Bullring",
    "Date": "2023-12-01T05:00:00.000Z",
    "State": "NV",
    "City": "Las Vegas",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.375,
    "Latitude": 36.2640599819706,
    "Longitude": -115.019403664406,
    "Recap": "x",
    "Status": "Permanent"
  },
  "216": {
    "Track": "Las Vegas Motor Speedway Outfield Road Course",
    "Date": "2023-12-03T05:00:00.000Z",
    "State": "NV",
    "City": "Las Vegas",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Latitude": 36.2675656820633,
    "Longitude": -115.017047456889,
    "Recap": "x",
    "Status": "Permanent"
  },
  "217": {
    "Track": "Caldwell Indoor Speedway",
    "Date": "2023-12-31T05:00:00.000Z",
    "State": "ID",
    "City": "Caldwell",
    "Type": "Arena",
    "Surface": "Dirt",
    "Latitude": 43.6559481355868,
    "Longitude": -116.671905311767,
    "Recap": "x",
    "Status": "Temporary"
  },
  "218": {
    "Track": "All-Tech Raceway",
    "Date": "2024-02-08T05:00:00.000Z",
    "State": "FL",
    "City": "Lake City",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Latitude": 29.9940402718067,
    "Longitude": -82.6118136821336,
    "Recap": "x",
    "Status": "Permanent"
  },
  "219": {
    "Track": "Nitrodome at Planet Hollywood",
    "Date": "2024-03-01T05:00:00.000Z",
    "State": "NV",
    "City": "Las Vegas",
    "Type": "Parking Lot",
    "Surface": "Mixed",
    "Latitude": 36.1106317636384,
    "Longitude": -115.16586137726,
    "Recap": "x",
    "Status": "Temporary"
  },
  "220": {
    "Track": "Texas Motor Speedway Dirt Track",
    "Date": "2024-04-05T04:00:00.000Z",
    "State": "TX",
    "City": "Fort Worth",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.4,
    "Status": "Permanent"
  },
  "221": {
    "Track": "Eagle Canyon Raceway",
    "Date": "2024-04-06T04:00:00.000Z",
    "State": "TX",
    "City": "Decatur",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "222": {
    "Track": "Lakeside Speedway",
    "Date": "2024-05-17T04:00:00.000Z",
    "State": "KS",
    "City": "Kansas City",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.4,
    "Recap": "x",
    "Status": "Permanent"
  },
  "223": {
    "Track": "Sweet Springs Motorsports Complex",
    "Date": "2024-05-19T04:00:00.000Z",
    "State": "MO",
    "City": "Sweet Springs",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.2,
    "Recap": "x",
    "Status": "Permanent"
  },
  "224": {
    "Track": "Humberstone Speedway",
    "Date": "2024-06-30T04:00:00.000Z",
    "State": "ON",
    "City": "Port Colborne",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Status": "Permanent"
  },
  "225": {
    "Track": "Ripley County Fairgrounds",
    "Date": "2024-07-24T04:00:00.000Z",
    "State": "IN",
    "City": "Osgood",
    "Type": "Fair",
    "Surface": "Dirt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "226": {
    "Track": "Brownstown Speedway",
    "Date": "2024-07-24T04:00:00.000Z",
    "State": "IN",
    "City": "Brownstown",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "227": {
    "Track": "Terre Haute Action Track",
    "Date": "2024-08-01T04:00:00.000Z",
    "State": "IN",
    "City": "Terre Haute",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.5,
    "Recap": "x",
    "Status": "Permanent"
  },
  "228": {
    "Track": "Federated Auto Parts Raceway at I-55",
    "Date": "2024-08-03T04:00:00.000Z",
    "State": "MO",
    "City": "Pevely",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Status": "Permanent"
  },
  "229": {
    "Track": "Bolton Fairgrounds",
    "Date": "2024-08-10T04:00:00.000Z",
    "State": "MA",
    "City": "Lancaster",
    "Type": "Fair",
    "Surface": "Dirt",
    "Recap": "x",
    "Status": "Temporary"
  },
  "230": {
    "Track": "Bolton Fairgrounds [Dirt Oval]",
    "Date": "2024-08-10T04:00:00.000Z",
    "State": "MA",
    "City": "Lancaster",
    "Type": "Fair",
    "Surface": "Dirt",
    "Recap": "x",
    "Status": "Temporary"
  },
  "231": {
    "Track": "MX101",
    "Date": "2024-08-25T04:00:00.000Z",
    "State": "NH",
    "City": "Epping",
    "Type": "Motocross",
    "Surface": "Dirt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "232": {
    "Track": "The Milwaukee Mile",
    "Date": "2024-08-31T04:00:00.000Z",
    "State": "WI",
    "City": "Milwaukee",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 1,
    "Recap": "x",
    "Status": "Permanent"
  },
  "233": {
    "Track": "Jefferson Speedway",
    "Date": "2024-08-31T04:00:00.000Z",
    "State": "WI",
    "City": "Cambridge",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Recap": "x",
    "Status": "Permanent"
  },
  "234": {
    "Track": "Jefferson Speedway [Inner Asphalt Oval]",
    "Date": "2024-08-31T04:00:00.000Z",
    "State": "WI",
    "City": "Cambridge",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "235": {
    "Track": "Angell Park Speedway",
    "Date": "2024-09-01T04:00:00.000Z",
    "State": "WI",
    "City": "Sun Prairie",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Recap": "x",
    "Status": "Permanent"
  },
  "236": {
    "Track": "508 International",
    "Date": "2024-09-08T04:00:00.000Z",
    "State": "MA",
    "City": "Charlton",
    "Type": "Motocross",
    "Surface": "Dirt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "237": {
    "Track": "Sportsdrome Speedway",
    "Date": "2024-09-14T04:00:00.000Z",
    "State": "IN",
    "City": "Clarksville",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "238": {
    "Track": "Sportsdrome Speedway [Asphalt Figure-8]",
    "Date": "2024-09-14T04:00:00.000Z",
    "State": "IN",
    "City": "Clarksville",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "239": {
    "Track": "Nashville Superspeedway",
    "Date": "2024-09-15T04:00:00.000Z",
    "State": "TN",
    "City": "Lebanon",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 1.33,
    "Status": "Permanent",
    "Character": "Minimal Character"
  },
  "240": {
    "Track": "Buttonwillow Raceway Park",
    "Date": "2024-11-16T05:00:00.000Z",
    "State": "CA",
    "City": "Buttonwillow",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Minimal Character"
  },
  "241": {
    "Track": "Kern County Raceway Park [Inner Asphalt Oval]",
    "Date": "2024-11-16T05:00:00.000Z",
    "State": "CA",
    "City": "Bakersfield",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Recap": "x",
    "Status": "Permanent"
  },
  "242": {
    "Track": "Tulare Thunderbowl Raceway",
    "Date": "2024-11-20T05:00:00.000Z",
    "State": "CA",
    "City": "Tulare",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Recap": "x",
    "Status": "Permanent"
  },
  "243": {
    "Track": "Las Vegas Strip Circuit",
    "Date": "2024-11-22T05:00:00.000Z",
    "State": "NV",
    "City": "Las Vegas",
    "Type": "Street",
    "Surface": "Asphalt",
    "Length": 3.853,
    "Recap": "x",
    "Status": "Temporary"
  },
  "244": {
    "Track": "Northwood Lake",
    "Date": "2025-03-01T05:00:00.000Z",
    "State": "NH",
    "City": "Northwood",
    "Type": "Lake",
    "Surface": "Ice",
    "Recap": "x",
    "Status": "Temporary",
    "Character": "Minimal Character"
  },
  "245": {
    "Track": "Boss Ice Arena",
    "Date": "2025-03-22T04:00:00.000Z",
    "State": "RI",
    "City": "Kingston",
    "Type": "Arena",
    "Surface": "Ice",
    "Recap": "x",
    "Status": "Temporary",
    "Character": "Minimal Character"
  },
  "246": {
    "Track": "Rockingham Speedway",
    "Date": "2025-04-18T04:00:00.000Z",
    "State": "NC",
    "City": "Rockingham",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.94,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "247": {
    "Track": "Wake County Speedway",
    "Date": "2025-04-18T04:00:00.000Z",
    "State": "NC",
    "City": "Raleigh",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Oozing with Character"
  },
  "248": {
    "Track": "Rockfish Speedway",
    "Date": "2025-04-19T04:00:00.000Z",
    "State": "NC",
    "City": "Raeford",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.2,
    "Recap": "x",
    "Status": "Permanent"
  },
  "249": {
    "Track": "US 36 Raceway",
    "Date": "2025-05-09T04:00:00.000Z",
    "State": "MO",
    "City": "Osborn",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Recap": "x",
    "Status": "Permanent"
  },
  "250": {
    "Track": "Kansas Speedway",
    "Date": "2025-05-10T04:00:00.000Z",
    "State": "KS",
    "City": "Kansas City",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 1.5,
    "Status": "Permanent"
  },
  "251": {
    "Track": "I-35 Speedway",
    "Date": "2025-05-10T04:00:00.000Z",
    "State": "MO",
    "City": "Winston",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Recap": "x",
    "Status": "Permanent"
  },
  "252": {
    "Track": "Double X Speedway",
    "Date": "2025-05-11T04:00:00.000Z",
    "State": "MO",
    "City": "California",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Recap": "x",
    "Status": "Permanent"
  },
  "253": {
    "Track": "Indianapolis Motor Speedway",
    "Date": "2025-05-23T04:00:00.000Z",
    "State": "IN",
    "City": "Speedway",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 2.5,
    "Status": "Permanent"
  },
  "254": {
    "Track": "Mt. Lawn Speedway",
    "Date": "2025-05-24T04:00:00.000Z",
    "State": "IN",
    "City": "New Castle",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.3,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Oozing with Character"
  },
  "255": {
    "Track": "Anderson Speedway",
    "Date": "2025-05-24T04:00:00.000Z",
    "State": "IN",
    "City": "Anderson",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.25,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "256": {
    "Track": "Atomic Speedway",
    "Date": "2025-05-26T04:00:00.000Z",
    "State": "OH",
    "City": "Chillicothe",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.3,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "257": {
    "Track": "Lime Rock Park",
    "Date": "2025-06-28T04:00:00.000Z",
    "State": "CT",
    "City": "Lakeville",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 1.5,
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "258": {
    "Track": "Oswego Speedway",
    "Date": "2025-06-28T04:00:00.000Z",
    "State": "NY",
    "City": "Oswego",
    "Type": "Racetrack",
    "Surface": "Asphalt",
    "Length": 0.625,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "259": {
    "Track": "Millstream Speedway",
    "Date": "2025-06-29T04:00:00.000Z",
    "State": "OH",
    "City": "Findlay",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.4,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Minimal Character"
  },
  "260": {
    "Track": "Gallatin Speedway",
    "Date": "2025-07-11T04:00:00.000Z",
    "State": "MT",
    "City": "Belgrade",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "261": {
    "Track": "Electric City Speedway",
    "Date": "2025-07-12T04:00:00.000Z",
    "State": "MT",
    "City": "Great Falls",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "262": {
    "Track": "Rapid Speedway",
    "Date": "2025-07-22T04:00:00.000Z",
    "State": "IA",
    "City": "Rock Rapids",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Minimal Character"
  },
  "263": {
    "Track": "Maquoketa Speedway",
    "Date": "2025-07-23T04:00:00.000Z",
    "State": "IA",
    "City": "Maquoketa",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "264": {
    "Track": "Dubuque Speedway",
    "Date": "2025-07-23T04:00:00.000Z",
    "State": "IA",
    "City": "Dubuque",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.375,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "265": {
    "Track": "The Dirt Track at Indianapolis Motor Speedway",
    "Date": "2025-07-24T04:00:00.000Z",
    "State": "IN",
    "City": "Speedway",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.2,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "266": {
    "Track": "US 24 Speedway",
    "Date": "2025-07-26T04:00:00.000Z",
    "State": "IN",
    "City": "Logansport",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.167,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "267": {
    "Track": "Mohawk International Speedway",
    "Date": "2025-08-05T04:00:00.000Z",
    "State": "NY",
    "City": "Akwesasne",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.4,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "268": {
    "Track": "Capeway Rovers",
    "Date": "2025-08-24T04:00:00.000Z",
    "State": "MA",
    "City": "Carver",
    "Type": "Motocross",
    "Surface": "Dirt",
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Decent Character"
  },
  "269": {
    "Track": "Three County Fair",
    "Date": "2025-09-01T04:00:00.000Z",
    "State": "MA",
    "City": "Northampton",
    "Type": "Fair",
    "Surface": "Dirt",
    "Recap": "x",
    "Status": "Temporary",
    "Character": "Decent Character"
  },
  "270": {
    "Track": "Berlin Fair",
    "Date": "2025-09-11T04:00:00.000Z",
    "State": "CT",
    "City": "Berlin",
    "Type": "Fair",
    "Surface": "Dirt",
    "Recap": "x",
    "Status": "Temporary",
    "Character": "Decent Character"
  },
  "271": {
    "Track": "Hawkwye Downs Speedway (Dirt)",
    "Date": "2025-09-27T04:00:00.000Z",
    "State": "IA",
    "City": "Cedar Rapids",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.25,
    "Recap": "x",
    "Status": "Temporary",
    "Character": "A Lot of Character"
  },
  "272": {
    "Track": "Cole's County Speedway",
    "Date": "2025-09-28T04:00:00.000Z",
    "State": "IL",
    "City": "Mattoon",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.167,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "A Lot of Character"
  },
  "273": {
    "Track": "Glen Helen Raceway [Dirt]",
    "Date": "2025-11-08T05:00:00.000Z",
    "State": "CA",
    "City": "Glen Helen",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Recap": "x",
    "Status": "Permanent"
  },
  "274": {
    "Track": "Bakersfield Speedway at Kevin Harvick's Kern Raceway",
    "Date": "2025-11-25T05:00:00.000Z",
    "State": "CA",
    "City": "Bakersfield",
    "Type": "Racetrack",
    "Surface": "Dirt",
    "Length": 0.33,
    "Recap": "x",
    "Status": "Permanent",
    "Character": "Minimal Character"
  },
  "": {
    "Status": "Permanent"
  }
}
"""

print replace_iso_dates(input3)