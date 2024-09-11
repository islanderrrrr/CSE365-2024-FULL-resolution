#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

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
        char *envp[] = {"92=zlavxufbhv", NULL}; //环境设置
        char *argv[] = {"/challenge/run", NULL};
        execve(argv[0], argv, envp);
        // If execve returns, it must have failed
        perror("execve");
        exit(EXIT_FAILURE);
    } else {
        // Parent process
        waitpid(pid, NULL, 0);  // Wait for the child to finish
    }

    return 0;
}
