import argparse
print("Simulating model training...")

# Contoh penggunaan argumen untuk mode tes
parser = argparse.ArgumentParser()
parser.add_argument("--epochs", type=int, default=10)
parser.add_argument("--test-mode", action="store_true")
args = parser.parse_args()

if args.test_mode:
    print(f"Running in test mode for {args.epochs} epoch(s).")
else:
    print(f"Running full training for {args.epochs} epoch(s).")

print("Training script finished successfully.")