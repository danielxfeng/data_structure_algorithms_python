# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def swap_down(next_available_times, workers_id, length, i):
    index = i
    l = 2 * i + 1
    r = 2 * i + 2
    if (l < length) and \
            ((next_available_times[l] < next_available_times[index]) or
             (next_available_times[l] == next_available_times[index] and
             workers_id[l] < workers_id[index])):
        index = l

    if (r < length) and \
            ((next_available_times[r] < next_available_times[index]) or
             (next_available_times[r] == next_available_times[index] and
             workers_id[r] < workers_id[index])):
        index = r

    if i != index:
        next_available_times[i], next_available_times[index] = next_available_times[index], next_available_times[i]
        workers_id[i], workers_id[index] = workers_id[index], workers_id[i]
        swap_down(next_available_times, workers_id, length, index)
    return


def assign_jobs(n_workers, jobs):

    next_available_times = [0] * n_workers
    workers_id = list(range(n_workers))
    res = []

    for job in jobs:

        available_time, worker_id = next_available_times[0], workers_id[0]
        next_available_time = available_time + job
        res.append(AssignedJob(worker_id, available_time))

        if job == 0:
            continue

        next_available_times[0] = next_available_time
        swap_down(next_available_times, workers_id, n_workers, 0)
        # print("res", worker_id, available_time)

    return res


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
