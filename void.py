#!/usr/bin/env python3
"""
void - advanced utility for permanent deletion of files and folders.
void - продвинутая утилита для безвозвратного удаления файлов и папок.

Commands / Команды:
  void -delete folder --name <path>   - delete folder
  void -delete file   --name <path>   - delete file
  void -delf <folder>                 - simple folder delete (with confirmation)
  void -delfi <file>                  - simple file delete (with confirmation)
  void voneo                          - show neofetch-like info about void
  void -doc | --documentation         - open GUI window with documentation
  void -v | --version                 - show version
  void -h | --help                    - show help
"""

import os
import sys
import shutil
import argparse
import subprocess
import platform
from pathlib import Path

# Optional imports for better visuals
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class Fore:
        RED = ''; GREEN = ''; YELLOW = ''; CYAN = ''; RESET = ''
    class Style:
        BRIGHT = ''; RESET_ALL = ''

# GUI for documentation
try:
    import tkinter as tk
    from tkinter import scrolledtext
    HAS_TK = True
except ImportError:
    HAS_TK = False

VERSION = "2.2.0"
AUTHOR = "morozzz"

# ---------- Core deletion functions (optimized) / Базовые функции удаления (оптимизированы)
def is_system_protected(path: str) -> bool:
    """Check if path is a Windows system folder (protection)."""
    system_dirs = ["C:\\Windows", "C:\\System32", "C:\\Program Files", "C:\\Program Files (x86)"]
    try:
        abs_path = os.path.abspath(path)
        return any(abs_path.lower().startswith(sys_dir.lower()) for sys_dir in system_dirs)
    except:
        return False

def hard_delete_folder(path: str, force: bool = False) -> None:
    """Delete folder recursively without recycle bin."""
    target = Path(path)
    if not target.exists():
        raise FileNotFoundError(f"Folder '{path}' does not exist.")
    if not target.is_dir():
        raise NotADirectoryError(f"'{path}' is not a folder.")
    if is_system_protected(str(target)):
        raise PermissionError(f"Deleting system folder '{path}' is forbidden.")
    if force:
        shutil.rmtree(target, ignore_errors=True)
        if target.exists():
            raise OSError(f"Could not fully delete '{path}' even with force.")
    else:
        shutil.rmtree(target)   # direct system call, fast

def hard_delete_file(path: str, force: bool = False) -> None:
    """Delete file permanently."""
    target = Path(path)
    if not target.exists():
        raise FileNotFoundError(f"File '{path}' does not exist.")
    if not target.is_file():
        raise IsADirectoryError(f"'{path}' is not a file.")
    if force:
        try:
            os.chmod(target, 0o777)   # remove read-only attribute
        except:
            pass
    target.unlink()   # fast

def get_file_size_str(path: str) -> str:
    """Return human-readable size of a file (fast)."""
    try:
        size = os.path.getsize(path)
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} PB"
    except:
        return "unknown"

# ---------- Simple mode with confirmation (native-like) / Упрощённый режим с подтверждением
def simple_confirm_deletion(path: str, is_folder: bool) -> bool:
    """Show info and ask for confirmation (colorful)."""
    full_path = os.path.abspath(path)
    obj_type = "FOLDER" if is_folder else "FILE"
    if HAS_COLOR:
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}⚠️  WARNING!{Style.RESET_ALL}")
    print(f"You are about to permanently delete {obj_type}:")
    print(f"  {Fore.CYAN}{full_path}{Fore.RESET}")
    if os.path.exists(path):
        if not is_folder:
            size_str = get_file_size_str(full_path)
            print(f"  Size: {Fore.CYAN}{size_str}{Fore.RESET}")
        else:
            print(f"  {Fore.CYAN}(folder content will be fully removed){Fore.RESET}")
    else:
        print(f"  {Fore.RED}ERROR: object does not exist!{Fore.RESET}")
        return False
    answer = input(f"\n{Fore.YELLOW}Delete? [y/N]: {Fore.RESET}").strip().lower()
    return answer in ('y', 'yes', 'да')

def simple_mode(cmd: str, target: str):
    """
    Simplified deletion: -delf for folder, -delfi for file.
    Always asks for confirmation, no --force.
    """
    if cmd == "-delf":
        is_folder = True
    elif cmd == "-delfi":
        is_folder = False
    else:
        print(f"{Fore.RED}Unknown simple command: {cmd}{Fore.RESET}")
        print("Use: void -delf <folder>  or  void -delfi <file>")
        sys.exit(1)

    if not os.path.exists(target):
        print(f"{Fore.RED}Error: '{target}' does not exist in current directory.{Fore.RESET}")
        sys.exit(1)

    if is_folder and not os.path.isdir(target):
        print(f"{Fore.RED}Error: '{target}' is not a folder. Use -delfi for files.{Fore.RESET}")
        sys.exit(1)
    if not is_folder and not os.path.isfile(target):
        print(f"{Fore.RED}Error: '{target}' is not a file. Use -delf for folders.{Fore.RESET}")
        sys.exit(1)

    if is_folder and is_system_protected(os.path.abspath(target)):
        print(f"{Fore.RED}Error: deleting system folder is forbidden!{Fore.RESET}")
        sys.exit(1)

    if simple_confirm_deletion(target, is_folder):
        try:
            if is_folder:
                hard_delete_folder(target, force=False)
            else:
                hard_delete_file(target, force=False)
            print(f"{Fore.GREEN}✓ Successfully deleted: {target}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}✗ Deletion failed: {e}{Fore.RESET}")
            sys.exit(1)
    else:
        print(f"{Fore.CYAN}Deletion cancelled.{Fore.RESET}")

# ---------- voneo command (neofetch-like for void) / Команда voneo
def voneo():
    """Display fancy ascii/info about void."""
    info = f"""
{Fore.CYAN}   __     ___  __ _   
   \ \   / / \|  _ \  
    \ \ / / _ \ | | | 
     \ V / ___ \ |_| |
      \_/_/   \_\___/ 
{Fore.YELLOW}         void v{VERSION}{Fore.RESET}

{Style.BRIGHT}About:{Style.RESET_ALL}
  • Fast and permanent deletion utility
  • Author: {AUTHOR}
  • License: MIT
  • Platform: {platform.system()} {platform.release()}

{Style.BRIGHT}Features:{Style.RESET_ALL}
  • Full syntax: void -delete (folder|file) --name <path> [-f]
  • Simple mode: void -delf <folder> / void -delfi <file>
  • GUI documentation: void -doc
  • Protection against deleting system folders
  • Colored output (if colorama installed)

{Style.BRIGHT}Stats (approximate):{Style.RESET_ALL}
  • Written in Python {platform.python_version()}
  • Core deletion: direct OS calls (maximum speed)
  • Lines of code: ~350
"""
    print(info)

# ---------- GUI Documentation (tkinter) / Окно документации
def show_documentation_gui():
    """Open a centered tkinter window with full documentation."""
    if not HAS_TK:
        print(f"{Fore.RED}Error: tkinter not available. Install python-tk or use 'void -h' for help.{Fore.RESET}")
        return
    root = tk.Tk()
    root.title("void Documentation")
    root.geometry("600x500")
    # Center the window
    root.eval('tk::PlaceWindow . center')
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=25, font=("Consolas", 10))
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    doc_content = f"""
void Utility - Permanent Deletion Tool
=======================================
Version: {VERSION}
Author: {AUTHOR}

DESCRIPTION:
  void is a command-line utility designed for fast, permanent deletion
  of files and folders. It bypasses the recycle bin / trash can.

COMMANDS:
  Full syntax:
    void -delete folder --name <path>   (delete a folder)
    void -delete file   --name <path>   (delete a file)
    void -delete folder --name <path> -f (force, ignore some errors)

  Simple syntax (with confirmation):
    void -delf <folder>                 (delete folder in current directory)
    void -delfi <file>                  (delete file in current directory)

  Extra:
    void voneo                          (show info about void)
    void -doc | --documentation         (open this GUI window)
    void -v | --version                 (show version)
    void -h | --help                    (show command line help)

SAFETY:
  • System folders (C:\\Windows, etc.) cannot be deleted.
  • Simple mode asks for confirmation before deletion.
  • Force flag (-f) may help with read-only files/folders.

OPTIMIZATION:
  • Direct operating system calls (shutil.rmtree, os.remove).
  • No unnecessary disk scanning when deleting.
  • Minimal memory footprint.

EXAMPLES:
  void -delete folder --name C:\\Temp\\OldFolder
  void -delfi document.txt
  void voneo
"""
    text_area.insert(tk.END, doc_content)
    text_area.config(state=tk.DISABLED)
    root.mainloop()

# ---------- Main argument dispatcher (unified) / Главный диспетчер
def main():
    prog_name = os.path.basename(sys.argv[0]).lower()
    # If called as 'nativevoid' for compatibility, redirect to simple mode
    if prog_name == "nativevoid":
        # emulate nativevoid -delf / -delfi
        if len(sys.argv) < 2:
            print("Usage: nativevoid (-delf|-delfi) <target>")
            sys.exit(1)
        simple_mode(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "")
        return

    # Normal void command processing
    if len(sys.argv) < 2:
        print("void - type 'void -h' for help")
        return

    # Handle simple mode commands at top level
    first_arg = sys.argv[1]
    if first_arg in ("-delf", "-delfi"):
        if len(sys.argv) < 3:
            print(f"Usage: void {first_arg} <target>")
            sys.exit(1)
        simple_mode(first_arg, sys.argv[2])
        return

    if first_arg in ("voneo", "neofetch"):
        voneo()
        return

    if first_arg in ("-doc", "--documentation"):
        show_documentation_gui()
        return

    # For version and help we use argparse but handle manually to avoid conflicts
    if first_arg in ("-v", "--version"):
        print(f"void version {VERSION}")
        return

    if first_arg in ("-h", "--help"):
        show_help_text()
        return

    # Full syntax with -delete
    if first_arg == "-delete":
        parse_full_delete()
    else:
        print(f"Unknown command: {first_arg}")
        print("Use 'void -h' for help")
        sys.exit(1)

def parse_full_delete():
    """Parse the classic -delete syntax."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-delete", action="store_true")
    parser.add_argument("delete_type", choices=["folder", "file"])
    parser.add_argument("--name", required=True)
    parser.add_argument("-f", "--force", action="store_true")
    args, unknown = parser.parse_known_args(sys.argv[1:])
    try:
        if args.delete_type == "folder":
            hard_delete_folder(args.name, force=args.force)
            print(f"Folder '{args.name}' successfully deleted.")
        else:
            hard_delete_file(args.name, force=args.force)
            print(f"File '{args.name}' successfully deleted.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def show_help_text():
    help_text = f"""
void v{VERSION} - permanent deletion utility

Usage:
  Full syntax:
    void -delete folder --name <path>   [-f]
    void -delete file   --name <path>   [-f]

  Simple syntax (with confirmation):
    void -delf <folder>                 (delete folder in current directory)
    void -delfi <file>                  (delete file in current directory)

  Other:
    void voneo                          (show system info about void)
    void -doc | --documentation         (open GUI documentation)
    void -v | --version
    void -h | --help

Examples:
  void -delete folder --name C:\\Temp\\Old
  void -delfi myfile.txt
  void voneo

WARNING: Deletion is permanent and immediate. No recycle bin.
"""
    print(help_text)

if __name__ == "__main__":
    main()