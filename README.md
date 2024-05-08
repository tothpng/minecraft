# Hospedando Minecraft com o GitHub

#### Instalação

1. Crie uma conta no [GitHub](https://github.com/signup).
- Caso você já tenha uma conta, avance para o próximo passo.

2. Acesse meu [Repositório](https://github.com/tothpng/minecraft).
- Clique em "Fork".
- Em seguida, crie o nome do repositório.

3. Crie um novo [Codespace](https://github.com/codespaces/new).
- Em seguida, clique em `Repository` e selecione o fork.
- Depois, clique em `Machine type` e selecione a última opção.

4. Crie uma conta no [Ngrok](https://dashboard.ngrok.com/signup).
- Em seguida, clique em `Your Authtoken` e depois em `Copy`.

5. Abra seu Codespace. 
- Clique em `Terminal` ou `Ctrl + J`.
- Digite `./ngrok authtoken seutoken` e pressione enter.
- Passe o mouse em cima do arquivo ngrok.yml e abra ele `Ctrl + Clique`.
- Logo abaixo de `authtoken`, abra uma linha e cole isso `region: sa`.
- Agora feche o arquivo e volte no Terminal.
- Execute o comando `./ngrok tcp 25565`.
- Copie o ip fornecido em `Forwarding`.
- Pressione as teclas `Ctrl + Shift + '` para abrir um novo bash.
- Agora digite o seguinte comando; `./start.sh`.

# Dúvidas

#### Qual launcher de Minecraft você recomenda?

- [Sklauncher](https://skmedix.pl/downloads)

#### Posso jogar em Multiplayer?

- Sim, o servidor suporta jogabilidade multiplayer.
- O uso do Ngrok facilita a conexão dos jogadores ao servidor.
- Mantendo uma latência máxima de 150ms.

#### Quais versões são suportadas?

- Vanilla, Forge, Fabric e Bukkit/Spigot

#### Onde posso baixar as versões informadas?

- [Vanilla](https://mcversions.net/)
- [Forge](https://files.minecraftforge.net/net/minecraftforge/forge/)
- [Fabric](https://fabricmc.net/use/server/)
- [Bukkit/Spigot](https://papermc.io/downloads/paper)

## Autores

- [Toth](https://github.com/tothpng)
