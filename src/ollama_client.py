"""
Simple Ollama client using the CLI instead of the HTTP API.

This avoids issues with /api/generate returning 404 and still satisfies the
"local LLM via Ollama" requirement for your class project.
"""

import subprocess
import textwrap


def call_ollama(model: str, prompt: str) -> str:
    """
    Call `ollama run <model>` via the CLI and return the model's text output.

    Parameters
    ----------
    model : str
        The Ollama model name, e.g. "llama3".
    prompt : str
        The prompt to send to the model.

    Returns
    -------
    str
        The text response from the model.
    """
    cmd = ["ollama", "run", model]

    try:
        proc = subprocess.run(
            cmd,
            input=prompt,
            text=True,
            capture_output=True,
            check=True,
            encoding="utf-8",   # force UTF-8 decoding
            errors="replace",   # avoid UnicodeDecodeError on weird chars
        )
    except FileNotFoundError:
        raise RuntimeError(
            "Could not find the 'ollama' CLI. "
            "Make sure Ollama is installed and that 'ollama' works in this terminal."
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"Ollama CLI failed with exit code {e.returncode}.\n"
            f"STDOUT:\n{e.stdout}\n\nSTDERR:\n{e.stderr}"
        ) from e

    # Strip trailing whitespace so our callers get clean text.
    return proc.stdout.strip()


def main():
    """Quick sanity test."""
    test_prompt = textwrap.dedent(
        """
        In 2 short bullet points, explain what a probability distribution is.
        Keep each bullet under 25 words.
        """
    ).strip()

    print("[TEST] Calling Ollama CLI (llama3)...\n")
    response = call_ollama("llama3", test_prompt)
    print(response)


if __name__ == "__main__":
    main()
