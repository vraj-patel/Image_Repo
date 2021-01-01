from nltk.translate.bleu_score import corpus_bleu
actual = [[("white and black dog leaps through long grass in field").split()]]
predicted = [("dog field").split()]
print(actual)
print(predicted)

bleu_score_1 = corpus_bleu(actual, predicted, weights=(1, 0, 0, 0))
bleu_score_2 = corpus_bleu(actual, predicted, weights=(0.5, 0.5, 0, 0))
bleu_score_3 = corpus_bleu(actual, predicted, weights=(0.33, 0.33, 0.34, 0))
bleu_score_4 = corpus_bleu(actual, predicted, weights=(0.25, 0.25, 0.25, 0.25))

print(bleu_score_1, bleu_score_2, bleu_score_3, bleu_score_4)