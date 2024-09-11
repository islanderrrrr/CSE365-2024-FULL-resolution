#bash下先创建路径

mkdir -p /tmp/cdvguv

#c.intera_script
  
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>

void pwncollege() {
    // This is the required function
}

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        // Fork failed
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (pid == 0) {
        // Child process
        chdir("/tmp/cdvguv"); //定义当前路径
        char *envp[] = {NULL};
        char *argv[] = {"/challenge/run", NULL};            
        execve(argv[0], argv, envp);

        perror("execve");
        exit(EXIT_FAILURE);
    } else {
        
        waitpid(pid, NULL, 0); 
    }

    return 0;
}
