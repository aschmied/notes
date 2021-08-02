# The Java Memory Model

The memory space for a Java process is partitioned into regions: meta space, code cache, stacks, shared libraries, and heap. These are under-the-hood concepts. Your program does not need to worry about which space an object is in. The memory parameters are tunable, but your program typically does not need to change to accommodate a change in memory parameters.

## Meta Space

Where class definitions are stored.

## Code Cache

Where JIT-compiled code is stored.

## Stacks

Thread stacks.

## Shared Libraries

Native or Java?

## Heap

Where your Java objects are stored. For garbage collection, the heap is further partitioned into generations: the **young generation** contains recently allocated objects and the **old generation** contains objects that have been allocated for a while. The young generation is further partitioned into three regions: **eden**, **survivor 0** (S0), and **survivor 1** (S1). S0 and S1 are the same size.

New objects are allocated in **eden** space. When eden space is full, the JVM executes a **minor GC** to clean up young space: unreachable objects in eden and survivor spaces are destroyed; reachable objects are copied from eden space to survivor space and have their age incremented by 1; and any reachable objects in eden space that do not fit in survivor space are **prematurely promoted** to the old generation and have their age incremented by 1. Reachable objects in survivor space with age greater than the `MaxTenuringThreshold` are promoted to old space.

In each **minor GC**, one of the two survivor space regions is designated as the **target** and the other is emptied. The target swaps between S0 and S1 on each GC event.

The **default young region size** is 0.5 times the old generation size. The **default MaxTenuringThreshold** is 15.

### Getting Memory and GC Data

You can use `jstat` to examine heap and memory counters. Use `-gccapacity` to see the sizes of the different memory regions:

```
# jstat -gccapacity <pid>
...YGC    FGC   CGC
...   146287  1700     -
```

1 is the pid. The first few columns correspond to the memory regions named above. `MN` is minimum capcacity, `MX` is maximum capacity, and `C` is current capacity. Capacities are in MB. `YGC` is the number of minor GC events, `FGC` is the number of full GC events, and `CGC` is the number of concurrent garbage collections.

The new and old generations make up the heap, so:

```
NGCMN + OGCMN = Xms
NGCMX + OGCMX = Xmx
```

To see GC stats, use `-gcutil`:

```
# jstat -gcutil <pid>
  S0     S1     E      O      M     CCS    YGC     YGCT    FGC    FGCT    CGC    CGCT     GCT
 53.95   0.00  14.20  73.08  67.32  55.02 146250 13550.357  1699 3448.057     -        - 16998.414
```

The fist few columns show the percent of utilized space in the regions described above. The S in `CCS` is for "space" ([ref](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jstat.html)). `YGC`, `FGC`, and `CGC` are are as above. The `T` suffix means "time," so e.g. `YGCT` is the time spent on young GCs. `GCT` is total GC time.

Use the following to print the GC stats every second and reprint the header every 30 times:

```
jstat -gcutil -h30 1 1s 
```

* Current heap is S0C + S1C + EC + OGC
* Max heap is NGCMX + OGCMX
* Young generation is 0.5 * old generation
* NGCMX + OGCMX = 873792.0 + 1747648.0 = 2621440

## References
getting Java heap
[jstat](https://stackoverflow.com/a/12802597/2833126)
[jstat docs](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jstat.html)
[Java memory model](https://smarttechie.org/2016/08/15/understanding-the-java-memory-model-and-the-garbage-collection/)
[GC logging and tuning](https://smarttechie.org/2016/08/28/enabling-and-analysing-the-garbage-collection-log/)
[Heap param tuning](https://docs.oracle.com/cd/E19900-01/819-4742/abeik/index.html)
[VIRT vs RES vs SHR vs SWAP](https://stackoverflow.com/a/561450/2833126)
