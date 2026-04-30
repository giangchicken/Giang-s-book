# Customize Virtual Environment Name in Terminal Prompt

By default, activating a Python virtual environment shows its folder name (e.g. `(.venv)`) in your terminal.

This guide shows how to display the **project folder name instead**.

---

## Goal

**From:**
```
(.venv) user@host:~/projects/DeepTutor
```

**To:**
```
(DeepTutor) user@host:~/projects/DeepTutor
```

---

## Solution (Recommended)

Update your shell prompt (`PS1`) to dynamically use the project folder name.

### Step 1: Open your shell config
```bash
nano ~/.bashrc
```

### Step 2: Add this at the end
```bash
# Show project name instead of (.venv)
function venv_prompt() {
  if [[ -n "$VIRTUAL_ENV" ]]; then
    echo "($(basename $(dirname $VIRTUAL_ENV)))"
  fi
}

export PS1='$(venv_prompt) \u@\h:\w\$ '
```

### Step 3: Apply changes
```bash
source ~/.bashrc
```

---

## Notes

- Works with any virtual environment tool (`venv`, `uv`, `poetry`, etc.)
- No need to modify `.venv/bin/activate`
- Changes persist across environments

---

## Optional: Reset Environment
```bash
deactivate
rm -rf .venv
uv venv
source .venv/bin/activate
uv sync
```

---

## Summary

- Do **not** rename `.venv` or edit `activate`
- Customize the shell prompt instead
- Clean, reusable, and scalable approach