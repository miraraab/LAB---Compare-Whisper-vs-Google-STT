import jiwer
import json

def calculate_wer(reference, hypothesis):
    transformation = jiwer.Compose([
        jiwer.ToLowerCase(),
        jiwer.RemovePunctuation(),
        jiwer.RemoveMultipleSpaces(),
        jiwer.Strip(),
    ])
    ref_clean = transformation(reference)
    hyp_clean = transformation(hypothesis)
    output = jiwer.process_words(ref_clean, hyp_clean)
    results = {
        "wer": output.wer,
        "accuracy": 1 - output.wer,
        "substitutions": output.substitutions,
        "insertions": output.insertions,
        "deletions": output.deletions,
        "hits": output.hits,
        "reference_words": len(ref_clean.split()),
        "hypothesis_words": len(hyp_clean.split())
    }
    return results
