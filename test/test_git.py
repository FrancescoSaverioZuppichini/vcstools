        self.root_directory = tempfile.mkdtemp()
        self.directories = dict(setUp=self.root_directory)
        self.remote_path = os.path.join(self.root_directory, "remote")
        os.makedirs(self.remote_path)
        subprocess.check_call(["git", "init"], cwd=self.remote_path)
        subprocess.check_call(["touch", "fixed.txt"], cwd=self.remote_path)
        subprocess.check_call(["git", "add", "*"], cwd=self.remote_path)
        subprocess.check_call(["git", "commit", "-m", "initial"], cwd=self.remote_path)
        subprocess.check_call(["git", "tag", "test_tag"], cwd=self.remote_path)
        po = subprocess.Popen(["git", "log", "-n", "1", "--pretty=format:\"%H\""], cwd=self.remote_path, stdout=subprocess.PIPE)
        subprocess.check_call(["touch", "modified.txt"], cwd=self.remote_path)
        subprocess.check_call(["touch", "modified-fs.txt"], cwd=self.remote_path)
        subprocess.check_call(["git", "add", "*"], cwd=self.remote_path)
        subprocess.check_call(["git", "commit", "-m", "initial"], cwd=self.remote_path)
        po = subprocess.Popen(["git", "log", "-n", "1", "--pretty=format:\"%H\""], cwd=self.remote_path, stdout=subprocess.PIPE)
        subprocess.check_call(["touch", "deleted.txt"], cwd=self.remote_path)
        subprocess.check_call(["touch", "deleted-fs.txt"], cwd=self.remote_path)
        subprocess.check_call(["git", "add", "*"], cwd=self.remote_path)
        subprocess.check_call(["git", "commit", "-m", "modified"], cwd=self.remote_path)
        po = subprocess.Popen(["git", "log", "-n", "1", "--pretty=format:\"%H\""], cwd=self.remote_path, stdout=subprocess.PIPE)
        subprocess.check_call(["git", "tag", "last_tag"], cwd=self.remote_path)
        
        
    
        local_path = os.path.join(self.root_directory, "ros")
        url = self.remote_path
        client = GitClient(local_path)
        self.assertFalse(client.path_exists())
        self.assertFalse(client.detect_presence())
        self.assertTrue(client.checkout(url))
        self.assertEqual(client.get_url(), self.remote_path)
        local_path = os.path.join(self.root_directory, "ros")
        url = self.remote_path
        local_path = os.path.join(self.root_directory, "ros")
        url = self.remote_path

        local_path = os.path.join(self.root_directory, "ros")
        url = self.remote_path

        self.readonly_path = os.path.join(self.root_directory, "readonly")
        from vcstools.git import GitClient
        client = GitClient(self.readonly_path)
        self.assertTrue(client.checkout(self.remote_path, self.readonly_version))


