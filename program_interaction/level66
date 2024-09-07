#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <glob.h>
#include <libgen.h>
#include <string.h>

char* glob_embryoio() {
    glob_t result;
    glob("/challenge/run", 0, NULL, &result);
    return result.gl_pathv[0];
  /*
  glob_embryoio() 函数使用 glob() 函数从文件系统中查找路径匹配 /challenge/run 的文件路径，并返回第一个匹配的路径。
  glob() 是一个文件名匹配函数，类似于 shell 中的 * 通配符。这里假定 /challenge/run 是目标文件（程序）的路径。
  */
}

int pwncollege() {
        int fd1[2];
        int fd2[2];
        if (pipe(fd1) == -1) {
                printf("Error occured with opening a pipe1!\n");
                return 1;
        }
        if (pipe(fd2) == -1) {
                printf("Error occured with opening a pipe2!\n");
                return 1;
        }
  /*
  pipe(fd1) 和 pipe(fd2) 创建了两个管道，分别存储在 fd1 和 fd2 中。一个管道用于传输输入数据，另一个管道用于接收输出数据。
  */
  /*
  fork() 调用用于创建一个子进程。如果 fork() 返回 0，表示此进程是子进程；如果返回大于 0 的值，表示此进程是父进程。
该部分代码嵌套了两个 fork()，所以会产生两个子进程。
  */
        if (fork()){
                if(fork()) {
                        sleep(1);
                        close(fd1[0]);

                        char pass[10] = "lpnacevv\n";

                        write(fd1[1], pass, strlen(pass));
                        close(fd1[1]);

                        wait(NULL);
                }
                  /*
                  父进程首先创建两个子进程。
在父进程中，第二个 fork() 被执行，父进程随后通过 pipe 将字符串 "lpnacevv\n" 写入 fd1[1]，然后关闭写入端。
wait(NULL) 用于等待子进程执行完毕。
                  */
                else {
                        close(fd1[1]);

                        dup2(fd1[0], 0);
                        
                        close(fd2[0]);
                        dup2(fd2[1], 1);
                        dup2(fd2[1], 2);

                        execlp("rev", "rev", NULL);
                }
          /*
          这个子进程从 fd1[0] 读取父进程写入的内容，并将其输入重定向到标准输入。
然后将标准输出和标准错误输出都重定向到 fd2[1]，使其写入第二个管道。
最后，执行 rev 命令（字符串翻转），将父进程输入的字符串（lpnacevv\n）翻转后输出到管道。
          */
        }
        else {
                close(fd1[0]);
                close(fd1[1]);
                close(fd2[1]);
                dup2(fd2[0], 0);

                char* envp[] = {NULL};
                char* bin_path = glob_embryoio();
                char* base_name = basename(bin_path);

                execle(bin_path, base_name, NULL, envp);
        }
    }
/*
第二个子进程从 fd2[0] 读取第一个子进程的输出（翻转后的字符串）。
它使用 glob_embryoio() 查找到的路径执行外部程序，该程序的路径通过 glob 函数匹配 /challenge/run。
execle() 用于执行该程序，且通过 dup2(fd2[0], 0) 将标准输入重定向为第一个子进程（翻转后的字符串）输入。
*/

int main() {
    pwncollege();
}
