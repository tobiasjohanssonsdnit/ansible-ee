#!/usr/bin/env python

import ansible_runner
import sys

# run ansible/generic commands in interactive mode within container
out, err = ansible_runner.run_command(
    executable_cmd="ansible-playbook",
    cmdline_args=["/Users/tobias_sdnit/git/ansible-ee/project/test.yml", "-v"],
    input_fd=sys.stdin,
    output_fd=sys.stdout,
    error_fd=sys.stderr,
    cwd="/Users/tobias_sdnit/git/ansible-ee/",
    process_isolation=True,
    process_isolation_executable="docker",
    container_image="quay.io/tobiasjohanssonsdnit/ansible-ee",
)
