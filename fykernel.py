import subprocess

from ipykernel.kernelbase import Kernel


class EchoKernel(Kernel):
    implementation = 'Echo'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {'mimetype': 'text/plain'}
    banner = "Echo kernel - as useful as a parrot"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            # print(code)
            # Combine stdout and stderr into one PIPE
            p = subprocess.Popen(code, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            for line in p.stdout:
                line = line.decode()
                # print(line)
                stream_content = {'name': 'stdout', 'text': line}
                self.send_response(self.iopub_socket, 'stream', stream_content)

        return {
            'status': 'ok',
            # The base class increments the execution count
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {},
        }

    def do_complete(self, code, cursor_pos):
        # print(code)
        # print(cursor_pos)
        return {
            'status': 'ok',
            'matches': ['foo', 'bar'],
            'cursor_start': cursor_pos,
            'cursor_end': cursor_pos,
            'metadata': {}
        }


if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=EchoKernel)
