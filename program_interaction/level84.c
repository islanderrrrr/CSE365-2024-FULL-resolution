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
        char *envp[] = {NULL};
        char *argv[] = {"/challenge/run", NULL};

        chdir("/tmp/hyrijs"); //改变当前目录
        //打开gumtdf并重定向输入
        int fd = open("gumtdf", O_RDONLY); 
        if (fd == -1) {
            perror("Failed to open gumtdf");
            exit(1);
        }
        dup2(fd, STDIN_FILENO);  //重定向输入进gumtdf文件
        close(fd);              

        execve(argv[0], argv, envp);

        perror("execve");
        exit(EXIT_FAILURE);
    } else {
        
        waitpid(pid, NULL, 0); 
    }

    return 0;
}
