import os
import tempfile
from zipfile import ZipFile

import gdown

SUPPORTED_DATASETS = ['pun_of_the_day', 'one_liners', 'reddit_jokes_last_laught', 'short_jokes', 'funlines', 'human_microedit']

USER_HOME = os.getenv('HOME')
DATA_PATH = os.path.join(USER_HOME, 'hri_tools_data/')


def downlaod():
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        
        url = os.getenv('HRI_URL')
        password = os.getenv('HRI_PASSWORD')
        password = bytes(password, 'utf-8')
        
        output = os.path.join(tmpdirname, 'dataset.zip')
        gdown.download(url, output, quiet=False, fuzzy=True)

        with ZipFile(output) as zf:
            zf.extractall(
                path=DATA_PATH,
                pwd=password
            )
        
        print('DONE!')



