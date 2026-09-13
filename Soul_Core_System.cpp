#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>

class SoulCore {
private:
    float integrity;
    float entropy;
    std::string state;

public:
    SoulCore(float init_integrity = 100.0f, float init_entropy = 0.0f, std::string init_state = "ACTIVE") 
        : integrity(init_integrity), entropy(init_entropy), state(init_state) {}

    void executeSubroutine(float cost) {
        entropy += cost;
        integrity = std::max(0.0f, integrity - (cost * 0.5f));
        
        if (integrity <= 15.0f) {
            state = "CRITICAL_CORRUPTION";
        } else if (entropy >= 80.0f) {
            state = "OVERHEAT";
        }
    }

    void toJson() const {
        std::cout << "{\"integrity\": " << integrity 
                  << ", \"entropy\": " << entropy 
                  << ", \"state\": \"" << state << "\"}\n";
    }
};

int main(int argc, char* argv[]) {
    // Default starting values (can be expanded to load from a state file)
    float integrity = 100.0f;
    float entropy = 0.0f;
    std::string state = "ACTIVE";

    float cost = 0.0f;
    if (argc > 1) {
        cost = std::atof(argv[1]);
    }

    SoulCore gem(integrity, entropy, state);
    if (cost > 0.0f) {
        gem.executeSubroutine(cost);
    }

    gem.toJson();
    return 0;
}
