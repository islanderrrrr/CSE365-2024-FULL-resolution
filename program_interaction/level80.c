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
        char *argv[] = {"/challenge/run", "arg1", "arg2", "arg3", "arg4", "arg5", "arg6", "arg7", "arg8", "arg9", "arg10", "arg11", "arg12", "arg13", "arg14", "arg15", "arg16", "arg17", "arg18", "arg19", "arg20", "arg21", "arg22", "arg23", "arg24", "arg25", "bhpdfkejkp", NULL};
        execve(argv[0], argv, NULL);
        // If execve returns, it must have failed
        perror("execve");
        exit(EXIT_FAILURE);
    } else {
        // Parent process
        int status;
        waitpid(pid, &status, 0);  // Wait for the child to finish
    }

    return 0;
}
