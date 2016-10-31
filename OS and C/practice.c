#include "practive.h"

char *get_human_readable(int given_flag, flagType flags[], int size);

int main()
{
    const flagType flags[] =
    {
        { PF_EXITING, "PF_EXITING" },
        { PF_EXITPIDONE, "PF_EXITPIDONE" },
        { PF_VCPU, "PF_VCPU" },
        { PF_WQ_WORKER, "PF_WQ_WORKER" },
        { PF_FORKNOEXEC, "PF_FORKNOEXEC" },
        { PF_MCE_PROCESS, "PF_MCE_PROCESS" },
        { PF_SUPERPRIV, "PF_SUPERPRIV" },
        { PF_DUMPCORE, "PF_DUMPCORE" },
        { PF_SIGNALED, "PF_SIGNALED" },
        { PF_MEMALLOC, "PF_MEMALLOC" },
        { PF_NPROC_EXCEEDED, "PF_NPROC_EXCEEDED" },
        { PF_USED_MATH, "PF_USED_MATH" },
        { PF_USED_ASYNC, "PF_USED_ASYNC" },
        { PF_NOFREEZE, "PF_NOFREEZE" },
        { PF_FROZEN, "PF_FROZEN" },
        { PF_FSTRANS, "PF_FSTRANS"},
        { PF_KSWAPD, "PF_KSWAPD"},
        { PF_MEMALLOC_NOIO, "PF_MEMALLOC_NOIO" },
        { PF_LESS_THROTTLE, "PF_LESS_THROTTLE" },
        { PF_KTHREAD, "PF_KTHREAD", "I am a kernel thread" },
        { PF_RANDOMIZE, "PF_RANDOMIZE", "randomize virtual address space" },
        { PF_SWAPWRITE, "PF_SWAPWRITE", "Allowed to write to swap" },
        { PF_SPREAD_PAGE, "PF_SPREAD_PAGE" },
        { PF_SPREAD_SLAB, "PF_SPREAD_SLAB" },
        { PF_NO_SETAFFINITY, "PF_NO_SETAFFINITY" },
        { PF_SUSPEND_TASK, "PF_SUSPEND_TASK" },
        { PF_FREEZER_SKIP, "PF_FREEZER_SKIP" },
        { PF_MUTEX_TESTER, "PF_MUTEX_TESTER" },
        { PF_MCE_EARLY, "PF_MCE_EARLY" },
    };

    int size = 30;
    unsigned int given_flag = 12;
    get_flags(flags, given_flag, size);
    return 0;
}

void get_flags(flagType flags[], unsigned int given_flag, int size)
{
    int int_flag;
    printf("\nFlags for %d\n", given_flag);
    char* for_human;
    while (given_flag)
    {
        int_flag = given_flag & (~ (given_flag - 1));
        printf("%d ", int_flag);
        given_flag = given_flag ^ int_flag;
        for_human = get_human_readable(int_flag, flags, size);
        if (strcmp(for_human, "xxNULL") != 0)
        {
            printf("%s\n", for_human);
        }
    }
}

char *get_human_readable(int given_flag, flagType flags[], int size )
{
    for (int i=0; i < size; i++)
    {
        if (flags[i].flagCode == given_flag)
        {
            return flags[i].flagString;
        }
    }
    return "xxNULL";
}
    /*
    [('0x00000004', 4), ('0x00000008', 8), ('0x00000010', 16), ('0x00000020', 32), ('0x00000040', 64),
    ('0x00000080', 128), ('0x00000100', 256), ('0x00000200', 512), ('0x00000400', 1024), ('0x00000800', 2048),
    ('0x00001000', 4096), ('0x00004000', 16384), ('0x00008000', 32768), ('0x00010000', 65536), ('0x00020000', 131072),
    ('0x00040000', 262144), ('0x00080000', 524288), ('0x00100000', 1048576), ('0x00200000', 2097152), ('0x00400000', 4194304),
    ('0x00800000', 8388608), ('0x01000000', 16777216), ('0x02000000', 33554432), ('0x04000000', 67108864),
    ('0x08000000', 134217728), ('0x20000000', 536870912), ('0x40000000', 1073741824), ('0x80000000', 2147483648)]
    */
