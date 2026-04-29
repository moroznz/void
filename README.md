
# void

**void** — advanced command-line utility for **permanent deletion of files and folders**.  
A fast, lightweight and practical tool for users who need direct deletion **without Recycle Bin / Trash**.

- Version: 2.2.0  
- Author: morozzz  
- License: MIT  

---

# 🇷🇺 Русский

## Описание

`void` — консольная утилита для безвозвратного удаления файлов и папок.  
Она удаляет объекты напрямую через системные вызовы, минуя корзину.

Подходит для:

- очистки временных файлов;
- удаления больших директорий;
- автоматизации через скрипты;
- быстрой очистки рабочих каталогов;
- администрирования системы;
- использования в терминале Windows / Linux.

---

## Возможности

### Постоянное удаление файлов и папок

```bash
void -delete file --name file.txt
void -delete folder --name old_folder
```

### Упрощённый режим с подтверждением

```bash
void -delf folder_name
void -delfi file.txt
```

### Принудительное удаление

```bash
void -delete folder --name locked_folder -f
```

### Защита системных папок

Утилита блокирует удаление важных системных директорий Windows:

- `C:\Windows`
- `C:\System32`
- `C:\Program Files`

### Красивый вывод информации

```bash
void voneo
```

### GUI документация

```bash
void -doc
```

---

## Где использовать

### Windows
Рекомендуемая платформа.  
Поддерживаются CMD, PowerShell, Windows Terminal.

### Linux
Работает в bash/zsh при установленном Python 3.

### macOS
Возможна работа через Python 3, если установлены зависимости.

---

## Зависимости

Необязательно, но рекомендуется:

```bash
pip install colorama
```

Для GUI документации:

```bash
tkinter
```

---

## Установка

```bash
git clone <[your-repo-url](https://github.com/moroznz/void)>
cd void
python void.py
```

Или добавить в PATH как `void`.

---

## Примеры

```bash
void -delete file --name secret.txt
void -delete folder --name temp
void -delf Downloads
void -delfi notes.txt
void voneo
```

---

## Важно

⚠️ Удаление необратимо.  
Файлы не попадают в корзину.

---

# 🇬🇧 English

## Description

`void` is a command-line utility for **permanent deletion** of files and folders.  
It removes targets directly using OS system calls and bypasses Recycle Bin / Trash.

Useful for:

- cleaning temporary files;
- deleting huge folders quickly;
- scripting and automation;
- workstation cleanup;
- system administration;
- terminal-based workflows.

---

## Features

### Permanent deletion

```bash
void -delete file --name file.txt
void -delete folder --name old_folder
```

### Simple confirmation mode

```bash
void -delf folder_name
void -delfi file.txt
```

### Force delete

```bash
void -delete folder --name locked_folder -f
```

### Protected system folders

Blocks deletion of critical Windows folders such as:

- `C:\Windows`
- `C:\System32`
- `C:\Program Files`

### Fancy info screen

```bash
void voneo
```

### GUI documentation

```bash
void -doc
```

---

## Recommended Platforms

### Windows
Best native experience with:

- CMD
- PowerShell
- Windows Terminal

### Linux
Works in bash/zsh with Python 3 installed.

### macOS
Supported through Python 3 environment.

---

## Dependencies

Optional:

```bash
pip install colorama
```

For GUI docs:

```bash
tkinter
```

---

## Installation

```bash
git clone <your-repo-url>
cd void
python void.py
```

Or add it to PATH as `void`.

---

## Examples

```bash
void -delete file --name report.txt
void -delete folder --name cache
void -delf Downloads
void -delfi todo.txt
void voneo
```

---

## Warning

⚠️ Deletion is immediate and irreversible.

---

# 🇫🇷 Français

## Description

`void` est un utilitaire en ligne de commande pour la **suppression définitive** de fichiers et dossiers.

Il supprime directement les éléments sans passer par la corbeille.

Idéal pour :

- nettoyer les fichiers temporaires ;
- supprimer rapidement de grands dossiers ;
- automatiser des tâches ;
- maintenance système ;
- utilisation en terminal.

---

## Fonctionnalités

### Suppression permanente

```bash
void -delete file --name file.txt
void -delete folder --name old_folder
```

### Mode simple avec confirmation

```bash
void -delf dossier
void -delfi fichier.txt
```

### Suppression forcée

```bash
void -delete folder --name locked_folder -f
```

### Protection des dossiers système

Empêche la suppression de dossiers critiques Windows :

- `C:\Windows`
- `C:\System32`
- `C:\Program Files`

### Écran d'information

```bash
void voneo
```

### Documentation GUI

```bash
void -doc
```

---

## Plateformes recommandées

### Windows
CMD, PowerShell, Windows Terminal.

### Linux
Fonctionne avec Python 3.

### macOS
Compatible avec environnement Python 3.

---

## Installation

```bash
git clone <your-repo-url>
cd void
python void.py
```

---

## Attention

⚠️ La suppression est définitive et immédiate.

---

# License

MIT License
