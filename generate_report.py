def generate_report(wer_results, audio_duration_sec, price_per_minute):
    audio_duration_min = audio_duration_sec / 60
    cost_single = audio_duration_min * price_per_minute

    lines = [
        "WHISPER STT EVALUATION REPORT",
        "==============================",
        "",
        "1. ACCURACY ANALYSIS",
        "WER:             " + str(round(wer_results["wer"]*100, 2)) + "%",
        "Accuracy:        " + str(round(wer_results["accuracy"]*100, 2)) + "%",
        "Substitutions:   " + str(wer_results["substitutions"]),
        "Insertions:      " + str(wer_results["insertions"]),
        "Deletions:       " + str(wer_results["deletions"]),
        "Korrekte Woerter: " + str(wer_results["hits"]) + " / " + str(wer_results["reference_words"]),
        "",
        "2. COST ANALYSIS",
        "Audio-Dauer:          " + str(round(audio_duration_sec, 1)) + " sec",
        "Kosten diese Datei:   $" + str(round(cost_single, 5)),
        "100 Meetings (1h/je): $" + str(round(100 * 60 * price_per_minute, 2)) + "/Monat",
        "500 Meetings (1h/je): $" + str(round(500 * 60 * price_per_minute, 2)) + "/Monat",
        "",
        "3. PERFORMANCE INSIGHTS",
        "[Eigene Beobachtungen: Fehlertypen, Fachbegriffe, Pausen, Akzent]",
        "",
        "4. RECOMMENDATIONS",
        "[Deploy Ja/Nein - unter welchen Bedingungen?]",
    ]
    return "\n".join(lines)
