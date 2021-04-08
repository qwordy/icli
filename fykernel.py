import subprocess

from ipykernel.kernelbase import Kernel

from completer import Completer


class EchoKernel(Kernel):
    implementation = 'Azure CLI'
    implementation_version = '0.1'
    language = 'Azure CLI'
    language_version = '0.1'
    language_info = {'mimetype': 'text/plain'}
    banner = "Azure CLI kernel"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.completer = Completer()

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
        # print(code, cursor_pos)
        default = {
            'status': 'ok',
            'matches': [],
            'cursor_start': 0,
            'cursor_end': cursor_pos,
            'metadata': {},
        }
        result = self.completer.complete(code[:cursor_pos])
        if result is None:
            return default
        return {
            'status': 'ok',
            'matches': result[0],
            'cursor_start': result[1],
            'cursor_end': cursor_pos,
            'metadata': result[2]
        }


if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=EchoKernel)
