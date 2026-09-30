# SiliconCopilot 🚀

**SiliconCopilot** is an on-device, NPU-accelerated AI hardware assistant designed for synthesizable Verilog design, testbench generation, and syntax/logic bug fixing. Built specifically for Snapdragon-powered PCs, it guarantees 100% semiconductor IP privacy, zero cloud latency, and complete offline availability.

---

## 🌟 Key Features

- **100% Local Execution:** Runs completely offline using local runtime engines, protecting sensitive RTL logic and hardware designs.
- **NPU Acceleration:** Offloads heavy neural network computations to the Snapdragon Hexagon NPU for sub-second responses and battery efficiency.
- **Specialized Workflows:**
  - **Verilog Code Generator:** Generates synthesizable RTL code from high-level specifications.
  - **Testbench Generator:** Creates automated testbenches complete with clock management, reset stimulus, and verification assertions.
  - **Syntax & Bug Fixer:** Automatically detects and resolves missing ports, blocking/non-blocking assignment bugs, and syntax errors.

---

## 🛠️ Tech Stack

- **UI Framework:** Streamlit
- **Local Inference Engine:** Ollama
- **Model:** `Qwen2.5-Coder:1.5b` (Optimized Code LLM)
- **Target Hardware:** Snapdragon-Powered PCs (Windows on ARM / Linux)

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your local machine:
- Python 3.10+
- [Ollama](https://ollama.com/)

### Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/SiliconCopilot.git](https://github.com/YOUR_USERNAME/SiliconCopilot.git)
   cd SiliconCopilot