package config

import (
	"log"
	"os"
	"strconv"

	"github.com/joho/godotenv"
)

type Config struct {
	Mode    string `yaml:"env" env:"ENV" env-required:"true"`
	Storage `yaml:"storage"`
}

type Storage struct {
	host     string `yaml:"host" env-required:"true"`
	port     uint16 `yaml:"port" env-required:"true"`
	db_name  string `yaml:"db_name" env-required:"true"`
	username string `yaml:"username" env-required:"true"`
	password string `yaml:"password" env-required:"true"`
}

type HTTPServer struct {
	Address string `yaml:"address" env-default:"localhost:8080"`
}

func MustLoad() *Config {

	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}

	var config Config

	config.Mode = os.Getenv("MODE")
	config.Storage.db_name = os.Getenv("DB_MAIN_NAME")
	config.Storage.host = os.Getenv("DB_MAIN_HOST")
	port, _ := strconv.Atoi(os.Getenv("DB_MAIN_PORT"))
	config.Storage.port = uint16(port)
	config.Storage.username = os.Getenv("DB_MAIN_USERNAME")
	config.Storage.password = os.Getenv("DB_MAIN_PASSWORD")

	return &config
}
