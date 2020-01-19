import logging
import subprocess
import os
import shutil
import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
news_sites_uids = ['portafolio', 'cnn']

def _extract():
    logger.info('Starting extract process')
    for news_site_uid in news_sites_uids:
        subprocess.run(['python', 'main.py', news_site_uid], cwd='./extract')
        path = './extract'
        file = _search_file(path, news_site_uid)
        _move_file(path + '/' + file, './files/dirty_files/' + file)


def _transform():
    logger.info('Starting transform process')
    
    for news_site_uid in news_sites_uids:
    	now = datetime.datetime.now().strftime('%Y_%m_%d')
    	file_name = f'{news_site_uid}_{now}_articles.csv'
    	dirty_data_filename = _search_file('./files/dirty_files', file_name)
    	clean_data_filename = f'clean_{dirty_data_filename}'
    	subprocess.run(['python', 'main.py', dirty_data_filename], cwd='./transform')
    	_move_file('./transform/' + clean_data_filename, './files/clean_files/' + clean_data_filename)


def _load():
    logger.info('Starting load process')
    
    for news_site_uid in news_sites_uids:
    	now = datetime.datetime.now().strftime('%Y_%m_%d')
    	file_name = f'{news_site_uid}_{now}_articles.csv'
    	clean_data_filename = _search_file('./files/clean_files', file_name)
    	subprocess.run(['python', 'base.py', clean_data_filename], cwd='./load')
    	# _remove_file('./load', clean_data_filename)


def _remove_file(path, file):
    logger.info(f'Removing file {file}')
    os.remove(f'{path}/{file}')


def _search_file(path, file_match):
    logger.info('Searching file')
    for rutas in list(os.walk(path))[0]:
        if len(rutas) > 1:
            for file in rutas:
                if file_match in file:
                    return file
    return None


def _move_file(origen, destino):
    logger.info('Moving file')
    shutil.move(origen, destino)


def main():
    try:
        logger.info('Starting ETL process')
        _extract()
        _transform()
        _load()
        logger.info('ETL process finished')
    except FileNotFoundError as err:
        logger.warning(str(err))
    except Exception as e:
        logger.warning('Process Error')
        logger.warning(str(e))

if __name__ == '__main__':
    main()