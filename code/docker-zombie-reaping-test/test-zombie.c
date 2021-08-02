#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <time.h>
#include <unistd.h>

void test();
void test_nested();
void start_child_of_child();

int main()
{
  setbuf(stdout, NULL);
  // test();
  test_nested();
  return 0;
}

void test()
{
  pid_t pid;

  pid = fork();
  if (pid > 0) {
  	printf("in parent\n");
    printf("child pid: %d\n", pid);
    time_t start_time = time(NULL);
    while (1) {
      time_t duration = time(NULL) - start_time;
      printf("running for %d:%d\n", duration / 60, duration % 60);
      sleep(10);
    }
  } else {
    printf("in child. simulating crash after exec\n");
    execlp( "false", NULL );
  }
}

void test_nested()
{
  pid_t pid;

  pid = fork();
  if (pid > 0) {
    printf("in parent\n");
    printf("child pid: %d\n", pid);
    time_t start_time = time(NULL);
    while (1) {
      time_t duration = time(NULL) - start_time;
      printf("running for %d:%d\n", duration / 60, duration % 60);
      sleep(10);
    }
  } else {
    start_child_of_child();
  }
}

void start_child_of_child()
{
  pid_t pid;

  pid = fork();
  if (pid > 0) {
    printf("in child. child of child pid: %d. exiting immediately to orphan child of child\n", pid);
  } else {
    printf("in child of child. sleeping then simulating crash after exec\n");
    sleep(30);
    execlp( "false", NULL );
  }
}
