# Safety and write ownership

Treat pre-existing staged, unstaged, and untracked work as user-owned. One implementation owner per change set; never overlap write scopes. Do not alter generated files, secrets, or external systems without explicit authorization. Use task-specific ignored workspace locations for temporary artifacts.

