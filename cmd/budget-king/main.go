package main

import (
	config_pkg "budget-king/internal/config"
	"log/slog"
	"os"
)

func main() {
	config := config_pkg.MustLoad()
	logger := setupLogger(config.Mode)
	logger.Info("staring budget-king-api", slog.String("mode", config.Mode))
	logger.Debug("debug messages are enabled")
}

const (
	modeLocal = "local"
	modeDev   = "dev"
	modeProd  = "prod"
)

func setupLogger(mode string) *slog.Logger {
	var logger *slog.Logger

	switch mode {
	case modeLocal:
		logger = slog.New(
			slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}),
		)
	case modeDev:
		logger = slog.New(
			slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}),
		)
	case modeProd:
		logger = slog.New(
			slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelInfo}),
		)

	}
	return logger
}
