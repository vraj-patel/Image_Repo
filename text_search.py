from nltk.translate.bleu_score import corpus_bleu
import shutil
import os

def search(search_text):
    search_text = [search_text.split()]

    results = {}

    with open('./Upload_Folder/descriptions.txt', 'r') as file:
        for line in file:
            line = line.split()
            image_path = line[0] + '.jpg'
            caption = [[line[1:]]]

            bleu_score_1 = corpus_bleu(caption, search_text, weights=(1, 0, 0, 0))
            bleu_score_2 = corpus_bleu(caption, search_text, weights=(0.5, 0.5, 0, 0))
            bleu_score_3 = corpus_bleu(caption, search_text, weights=(0.33, 0.33, 0.34, 0))
            bleu_score_4 = corpus_bleu(caption, search_text, weights=(0.25, 0.25, 0.25, 0.25))

            total_score = bleu_score_1 + bleu_score_2 + bleu_score_3 + bleu_score_4

            if image_path in results and total_score > results[image_path]: results[image_path] = total_score
            elif image_path not in results: results[image_path] = total_score

    top_results = sorted(results, key=results.get, reverse=True)[:10]

    for f in os.listdir('Search_Results'):
        os.remove(os.path.join('Search_Results', f))

    for file_name in top_results:
        shutil.copyfile('./Upload_Folder/images/'+file_name, './Search_Results/'+file_name)
    
    return top_results