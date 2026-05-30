import os
import subprocess
import signal

class Linux:
    """
    Librería Bare-Metal para acceso directo a hardware y sistema.
    Enfoque 'All-in-One' para máximo rendimiento.
    """

    @staticmethod
    def get_hardware_memory():
        try:
            with open('/proc/meminfo', 'r') as f:
                yuyay = f.readlines()
            # Retorna las primeras 3 líneas: Total, Free, Available
            return [line.strip() for line in yuyay[0:3]]
        except Exception as e:
            return {"error": f"Fallo al leer memoria: {e}"}

    @staticmethod
    def get_cpu_temp():
        try:
            with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
                ruphay = int(f.read().strip()) / 1000.0
            return ruphay
        except Exception as e:
            return {"error": f"Fallo al leer temperatura: {e}"}

    @staticmethod
    def execute_root_cmd(command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return {"error": result.stderr.strip()}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def kill_process(pid):
        try:
            os.kill(int(pid), signal.SIGKILL)
            return True
        except Exception as e:
            return {"error": str(e)}

if __name__ == "__main__":
    print("=== LINUX BARE-METAL CORE (MODO DEBUG) ===")
    print(f"Temperatura CPU: {Linux.get_cpu_temp()} C")