import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from datetime import datetime

class GitHubRepoInfo:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Repository Info")
        self.root.geometry("500x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        
        title_label = ttk.Label(main_frame, text="GitHub Repository Information", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        
        repo_label = ttk.Label(main_frame, text="Repository Name:")
        repo_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.repo_entry = ttk.Entry(main_frame, width=40)
        self.repo_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        self.repo_entry.bind('<Return>', lambda event: self.get_repo_info())
        
        
        examples_label = ttk.Label(main_frame, text="Examples: apple/swift, kubernetes/kubernetes", 
                                  font=("Arial", 9), foreground="gray")
        examples_label.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
       
        self.get_info_btn = ttk.Button(main_frame, text="Get Repository Info", 
                                      command=self.get_repo_info)
        self.get_info_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        
        self.status_label = ttk.Label(main_frame, text="", foreground="blue")
        self.status_label.grid(row=5, column=0, columnspan=2, pady=5)
        
        
        main_frame.columnconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
    
    def get_repo_info(self):
        repo_name = self.repo_entry.get().strip()
        
        if not repo_name:
            messagebox.showerror("Error", "Please enter a repository name")
            return
        
        
        if '/' not in repo_name:
            messagebox.showerror("Error", "Please enter repository in format: owner/repo")
            return
        
        self.get_info_btn.config(state='disabled')
        self.progress.start()
        self.status_label.config(text="Fetching repository information...")
        
        try:
            
            url = f"https://api.github.com/repos/{repo_name}"
            response = requests.get(url)
            
            if response.status_code == 200:
                repo_data = response.json()
                
                
                owner = repo_data.get('owner', {})
                
                
                result_data = {
                    'company': owner.get('company'),
                    'created_at': owner.get('created_at'),
                    'email': owner.get('email'),
                    'id': owner.get('id'),
                    'name': owner.get('login'),
                    'url': owner.get('url')
                }
                
                
                self.save_to_file(result_data, repo_name)
                
                
                self.status_label.config(text="Information saved successfully!", foreground="green")
                messagebox.showinfo("Success", f"Repository information saved to 'github_info.json'")
                
            elif response.status_code == 404:
                messagebox.showerror("Error", "Repository not found")
                self.status_label.config(text="Repository not found", foreground="red")
            else:
                messagebox.showerror("Error", f"API Error: {response.status_code}")
                self.status_label.config(text=f"Error: {response.status_code}", foreground="red")
                
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Network error: {str(e)}")
            self.status_label.config(text="Network error", foreground="red")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {str(e)}")
            self.status_label.config(text="Unexpected error", foreground="red")
        finally:
            self.get_info_btn.config(state='normal')
            self.progress.stop()
    
    def save_to_file(self, data, repo_name):
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"github_info_{timestamp}.json"
        
        
        output_data = {
            'repository': repo_name,
            'fetched_at': datetime.now().isoformat(),
            'owner_info': data
        }
        
       
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        
        with open('github_info.json', 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

def main():
    root = tk.Tk()
    app = GitHubRepoInfo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
