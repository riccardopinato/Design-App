package factory.icons

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class FactoryIconMappingTest {
    @Test
    fun exactlyTwentyFourCanonicalIconsResolve() {
        assertEquals(24, FactoryIconKey.entries.size)
        FactoryIconKey.entries.forEach { semantic ->
            val vector = semantic.materialImageVector()
            assertTrue("invalid width for $semantic", vector.defaultWidth.value > 0f)
            assertTrue("invalid height for $semantic", vector.defaultHeight.value > 0f)
        }
    }

    @Test
    fun navigationBackIsAutoMirroredForRtl() {
        assertEquals(Icons.AutoMirrored.Filled.ArrowBack, FactoryIconKey.BACK.materialImageVector())
    }

    @Test
    fun semanticIdentifiersAreStable() {
        assertTrue(FactoryIconKey.entries.any { it.name == "CALENDAR" })
        assertTrue(FactoryIconKey.entries.any { it.name == "WARNING" })
        assertTrue(FactoryIconKey.entries.any { it.name == "SETTINGS" })
    }
}
