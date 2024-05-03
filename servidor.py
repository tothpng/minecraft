P=print
import requests as R,os # type: ignore
def D(repo_owner,repo_name,download_path='.'):
	H=f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest";D=R.get(H);A=''
	if D.status_code==200:
		I=D.json();E=I.get('assets')
		if E:
			F=E[0];G=F.get('browser_download_url')
			if G:
				A=os.path.join(download_path,F.get('name'))
				with open(A,'wb')as J:J.write(R.get(G).content)
				P(f"Download completo! Arquivo salvo como: {A}")
			else:P('Não foram encontrados arquivos para download no último lançamento.')
		else:P('Não foram encontrados ativos no último lançamento.')
	else:P('Erro ao obter informações sobre o último lançamento.')
	return A
E='elyxdev'
F='elyx-server'
A=D(E,F)
if A.split('.')[2]=='pyc':os.system(f"python3 {A}")
else:os.system(f"chmod +x {A}");os.system(f"{A}")
