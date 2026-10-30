plugins {
    kotlin("jvm") version "2.2.20"
    id("org.jetbrains.compose") version "1.9.1"
    id("org.jetbrains.kotlin.plugin.compose") version "2.2.20"
}

dependencies {
    implementation(compose.material)
    implementation(compose.material3)
    testImplementation(kotlin("test-junit"))
    testImplementation("junit:junit:4.13.2")
}

kotlin {
    jvmToolchain(17)
}
