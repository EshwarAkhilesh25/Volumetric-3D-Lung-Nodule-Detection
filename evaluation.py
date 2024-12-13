!pip install future
!mkdir -p /kaggle/working/luna_evaluation
!cp /kaggle/input/lung-nodule-3/noduleCADEvaluationLUNA16.py /kaggle/working/luna_evaluation/
%cd /kaggle/working/luna_evaluation/
!futurize --stage1 -w noduleCADEvaluationLUNA16.py
!futurize --stage2 -w noduleCADEvaluationLUNA16.py
import subprocess
import os

def main():
    # Define the input JSON files
    input_json_files = [
        '/kaggle/input/res80eval/result_80/result_luna16_fold0_80.json',
        '/kaggle/input/res80eval/result_80/result_luna16_fold1_80.json',
        '/kaggle/input/res80eval/result_80/result_luna16_fold2_80.json',
        '/kaggle/input/res80eval/result_80/result_luna16_fold3_80.json',
        '/kaggle/input/res80eval/result_80/result_luna16_fold4.json',
        '/kaggle/input/res80eval/result_80/result_luna16_fold5.json',
        '/kaggle/input/res80eval/result_80/result_luna16_fold6.json',
        '/kaggle/input/res80eval/result_80/result_luna16_fold7.json',
        '/kaggle/input/res80eval/result_80/result_luna16_fold8.json',
        '/kaggle/input/res80eval/result_80/result_luna16_fold9.json'
    ]

    # Define the output CSV filez
    output_csv_file = '/kaggle/working/result_luna16_all.csv'

    # Combine JSON results into a single CSV file
    subprocess.run(['python', '/kaggle/input/lung-nodule-3/lung_nodule_copy2/lung_nodule_ct_detection/scripts/luna16_post_combine_cross_fold_results.py', '-i'] + input_json_files + ['-o', output_csv_file])

    # Create the directory for evaluation scores if it doesn't exist
    eval_scores_dir = '/kaggle/working/eval_luna16_scores'
    os.makedirs(eval_scores_dir, exist_ok=True)
    # Define the paths for evaluation annotations
    annotations_csv = '/kaggle/input/lung-nodule-3/lung_nodule_copy2/lung_nodule_ct_detection/evaluationScript/annotations/annotations.csv'
    annotations_excluded_csv = '/kaggle/input/lung-nodule-3/lung_nodule_copy2/lung_nodule_ct_detection/evaluationScript/annotations/annotations_excluded.csv'
    seriesuids_csv = '/kaggle/input/lung-nodule-3/lung_nodule_copy2/lung_nodule_ct_detection/evaluationScript/annotations/seriesuids.csv'

    # Run the evaluation script
    subprocess.run([
        'python', '/kaggle/input/evalllll/noduleCADEvaluationLUNA16.py',
        annotations_csv,
        annotations_excluded_csv,
        seriesuids_csv,
        output_csv_file,
        eval_scores_dir
    ])

if __name__ == "__main__":
    main()
